'use strict'

module.exports = function (...args) {
  args.pop(); // remove Handlebars options object
  return args.join('');
};

