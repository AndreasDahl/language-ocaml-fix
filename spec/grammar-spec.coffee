path = require 'path'
grammarTest = require 'atom-grammar-test'

describe 'OCaml grammar', ->

  beforeEach ->
    # Ensure you're language package is loaded
    waitsForPromise ->
      atom.packages.activatePackage 'language-ocaml-fix',

  grammarTest(path.join(__dirname, 'ocaml.spec'))
  grammarTest(path.join(__dirname, 'ocaml_class.spec'))
  grammarTest(path.join(__dirname, 'ocaml_external.spec'))
  grammarTest(path.join(__dirname, 'ocaml_let_binding.spec'))
  grammarTest(path.join(__dirname, 'ocaml_type_definition.spec'))
