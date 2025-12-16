# Simple Data Catalog

A lightweight, LinkML‑based data catalog that can be generated and validated automatically via **Copier** templates and **GitHub Actions**.

---

## WARNING

***This project is pre-production. Backwards compatibility is not yet guaranteed.
While the ultimate goal for the project is to valdiate against [DCAT AP](https://op.europa.eu/en/web/eu-vocabularies/dcat-ap) this is currently not the case yet. As the remaining issues will be fixed, this might result in incompatibility with the current data format.***


## Table of Contents

1. [Adding Content to the Catalog](#adding-content-to-the-catalog)  
2. [Managing Repository Permissions](#managing-repository-permissions)  
3. [What Happens After a Push?](#what-happens-after-a-push)  
4. [Development Workflow (for reference)](#development-workflow)  

---

## Adding Content to the Catalog

All catalog metadata lives in `data-catalog/data-catalog.yaml`.  
The file follows a **LinkML** schema (see [simple_data_catalog_model](https://uuidea.github.io/simple_data_catalog_model/documentation/schema/index.html)).  

### 1. Datasets

```yaml
datasets:
  - identifier: ex:myDataset
    title: My Dataset
    publisher:
      name: My Organization
    contactPoint:
      hasEmail: contact@myorg.org
    status: draft
    theme:
      - ex:energy
      - ex:climate
    license:
      title: CC‑BY 4.0
    temporal:
      hasBeginning: "2024-01-01"
      hasEnd: "2024-12-31"
    inSeries: ex:mySeries
    distribution: ex:myDist
```

* **identifier** – must be a globally unique CURIE (e.g., `ex:myDataset`).  
* **distribution** – points to an entry in the `distributions` section.  

### 2. Distributions

```yaml
distributions:
  - identifier: ex:myDist
    format: csv
    accessURL: https://example.com/data/my-dataset.csv
    issued: "2024-11-01"
```

### 3. Data Services

```yaml
dataServices:
  - identifier: ex:myService
    title: Example API
    servesDataset:
      - ex:myDataset
    description: REST endpoint exposing the dataset
    endpointURL: https://api.example.com/v1/datasets/my-dataset
```

### 4. Concepts, Series, Metrics, QualityMeasurements

Add entries under the respective top‑level keys (`concepts`, `series`, `metrics`, `qualityMeasurements`) following the same pattern as above.  

**Tip:** Keep the YAML tidy by using the existing sections as templates. The `generate-datacatalog.sh` script (triggered by CI) will automatically render the yaml into the final TTL file, as well ass the published catalog.

---

## Managing Repository Permissions

Repository owners can control who can **commit**, **push**, and **merge** changes to the catalog.

| Permission | GitHub Setting | Recommended Role |
|------------|----------------|------------------|
| **Read**   | `Read` access  | All collaborators |
| **Write**  | `Write` access | Contributors who add/modify catalog entries |
| **Admin**  | `Admin` access | Project maintainers |

### Steps to Configure

1. **Branch protection**  
   - Go to **Settings → Branches → Add rule** (e.g., `main`).  
   - Enable **Require pull request reviews before merging**.  
   - Optionally require **status checks** (see next section).

2. **Team permissions** (if using an organization)  
   - In **Settings → Collaborators & teams**, create a team (e.g., `catalog‑editors`).  
   - Grant the team **Write** permission.

3. **Code owners** (optional)  
   - Add a `CODEOWNERS` file at the repository root:  

   ```text
   # CODEOWNERS
   # Users listed here must approve PRs that modify the catalog
   *.yaml @catalog-editors
   ```

   This forces review by the designated owners.

---

## What Happens After a Change Is Pushed?

1. **GitHub Actions Workflow** (`.github/workflows/catalog.yml`) runs automatically on every push to `main` (or on pull‑request merges).  
2. The workflow executes the following steps:
   - **Validate** the updated `data-catalog.yaml` using `linkml-validate`.  
   - **Render** the yaml file (`data-catalog.yaml`) into a TTL file via `linkml-convert`.  
   - **Commit** the generated `data-catalog.ttl` back to the repository (if the workflow is configured to do so).  
   - **Publish** the artifact (e.g., upload to a static site or an S3 bucket) so downstream users can fetch the latest catalog.

3. **If validation fails**, the workflow aborts and the CI status on the PR becomes **failed**. Reviewers must fix the YAML before merging.

4. **Successful runs** result in a green checkmark on the PR/commit, indicating the catalog is up‑to‑date and syntactically correct.

---

## Development Workflow (for reference)

```bash
# 1. Install dependencies (once)
uv sync

# 2. Run the generation script locally (optional)
bash template/scripts/generate-datacatalog.sh

# 3. Validate manually
uv run linkml-validate -s simple_data_catalog_model/src/simple_data_catalog_model/data-catalog.yaml data-catalog/data-catalog.yaml