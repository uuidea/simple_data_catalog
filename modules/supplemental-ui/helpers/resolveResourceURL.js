//  Solution by Dan Allen. See:
//  https://antora.zulipchat.com/#narrow/channel/282400-users/topic/Syntax.20for.20link.20to.20attachment.20in.20Antora.20.20UI.3F/near/395108921
//

'use strict'

module.exports = (spec, { data, hash: context }) => {
  if (!spec) return
  const { contentCatalog, page } = data.root
  if (page.component) {
    context = Object.assign({ component: page.component.name, version: page.version, module: page.module }, context)
  }
  const file = contentCatalog.resolveResource(spec, context, 'page', ['page', 'attachment', 'image'])
  if (file) return file.pub.url
}
