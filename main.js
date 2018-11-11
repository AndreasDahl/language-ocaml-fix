exports.activate = function() {
  if (!atom.grammars.addInjectionPoint) return

  atom.grammars.addInjectionPoint('source.ocamllex', {
    type: 'lexer_definition',

    language: (node) => 'ocaml',

    content: (node) => node.children
      .filter((child) => child.type == 'action')
      .map((node) => node.children[1])
  })

  atom.grammars.addInjectionPoint('source.ocamllex', {
    type: 'refill_handler',

    language: (node) => 'ocaml',

    content: (node) => node.children[2]
  })

  atom.grammars.addInjectionPoint('source.ocamllex', {
    type: 'lexer_case',

    language: (node) => 'ocaml',

    content: (node) => node.lastChild.children[1]
  })
}
