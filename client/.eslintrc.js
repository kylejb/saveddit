module.exports = {
  root: true,
  parser: '@typescript-eslint/parser', // Specifies the ESLint parser
  parserOptions: {
    ecmaVersion: 2020, // Allows for the parsing of modern ECMAScript features
    sourceType: 'module', // Allows for the use of imports
    ecmaFeatures: {
      jsx: true, // Allows for the parsing of JSX
      arrowFunctions: true,
    },
    tsconfigRootDir: __dirname,
    project: ['./tsconfig.json'],
  },
  settings: {
    react: {
      version: 'detect', // Tells eslint-plugin-react to automatically detect the version
    },
  },
  extends: [
    // Uses the recommended rules from @eslint-plugin-react
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    // Uses the recommended rules from the @typescript-eslint/eslint-plugin
    'plugin:@typescript-eslint/recommended',
    // Uses eslint-config-prettier to disable ESLint rules
    'plugin:prettier/recommended',
  ],
  plugins: ['@typescript-eslint', 'react', 'react-hooks', 'jest', 'prettier'],
  rules: {
    'react/jsx-filename-extension': [1, { "extensions": [".tsx", ".ts"] }],
    // suppress errors for missing 'import React' in files
    'react/react-in-jsx-scope': 'off',
    // https://eslint.org/docs/rules/comma-dangle
    'comma-dangle': 'off',
    // https://eslint.org/docs/rules/function-paren-newline
    'function-paren-newline': 'off',
    // https://eslint.org/docs/rules/global-require
    'global-require': 'off',
    // https://github.com/benmosher/eslint-plugin-import/blob/master/docs/rules/no-dynamic-require.md
    'import/no-dynamic-require': 'off',
    // https://eslint.org/docs/rules/no-inner-declarations// New rules
    'no-inner-declarations': 'off',
    'class-methods-use-this': 'off',
    'import/extensions': 'off',
    'import/prefer-default-export': 'off',
    '@typescript-eslint/explicit-function-return-type': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-var-requires': 'off',
  },
};
