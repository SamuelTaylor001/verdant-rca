const legacyCode = {
  "class-methods-use-this": 0,
};

module.exports = {
  // See https://github.com/torchbox/eslint-config-torchbox for rules.
  extends: "torchbox",
  parser: "babel-eslint",
  rules: {
    ...legacyCode,
  },
};
