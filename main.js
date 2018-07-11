exports.activate = function() {
  if (!atom.grammars.addInjectionPoint) return

  atom.grammars.addInjectionPoint('ocamllex', {
    type: 'lexer_definition',

    language: (node) => 'ocaml',

    content: (node) => node.children
      .filter((child) => child.type == 'action')
      .map((node) => node.children.find((child) => child.type == 'ocaml'))
  })

  atom.grammars.addInjectionPoint('ocamllex', {
    type: 'refill_handler',

    language: (node) => 'ocaml',

    content: (node) => node.children.find((child) => child.type == 'ocaml')
  })

  atom.grammars.addInjectionPoint('ocamllex', {
    type: 'lexer_case',

    language: (node) => 'ocaml',

    content: (node) => {
      const action = node.children.find((child) => child.type == 'action')
      return action.children.find((child) => child.type == 'ocaml')
    }
  })

  // atom.grammars.addInjectionPoint('ocamllex', {
  //   type: 'ocaml',
  //
  //   language: (node) => 'ocaml',
  //
  //   content: (node) => node
  // })
}
