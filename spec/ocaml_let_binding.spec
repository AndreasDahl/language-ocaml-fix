// SYNTAX TEST "source.ocaml"
let x = 1 in 2
//<- keyword.other.let_binding.ocaml
//    ^ punctuation.separator.assignment.ocaml
//        ^^ keyword.other.in.ocaml
//^^^^^^^^^^ meta.let_binding.ocaml
//          ^^ !meta.let_binding.ocaml

let x = 1 and y = 2 in 3
//<- keyword.other.let_binding.ocaml
//    ^ punctuation.separator.assignment.ocaml
//        ^^^ keyword.other.and.ocaml
//              ^ punctuation.separator.assignment.ocaml
//                  ^^ keyword.other.in.ocaml
//^^^^^^^^^^^^^^^^^^^^ meta.let_binding.ocaml
//                    ^^ !meta.let_binding.ocaml

let x = 1 and y = 2 and z = 3 in 4
//<- keyword.other.let_binding.ocaml
//    ^ punctuation.separator.assignment.ocaml
//        ^^^ keyword.other.and.ocaml
//              ^ punctuation.separator.assignment.ocaml
//                  ^^^ keyword.other.and.ocaml
//                        ^ punctuation.separator.assignment.ocaml
//                            ^^ keyword.other.in.ocaml
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.let_binding.ocaml
//                              ^^ !meta.let_binding.ocaml

let x = 1
//<- keyword.other.let_binding.ocaml
//    ^ punctuation.separator.assignment.ocaml
//^^^^^^^ meta.let_binding.ocaml
and y = 2
//<- keyword.other.and.ocaml
//^^^^^^^ meta.let_binding.ocaml
in 3
//<- keyword.other.in.ocaml
//<- meta.let_binding.ocaml
//^^ !meta.let_binding.ocaml
