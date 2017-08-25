// SYNTAX TEST "source.ocaml"
class ['a] foo = object end
//<- keyword.other.class-definition.ocaml
//      ^ storage.type.ocaml
//         ^^^ entity.name.type.class.ocaml
//^^^^^^^ meta.class.ocaml

class foo = object method bar x = x end
//          ^^^^^^ keyword.other.object-definition.ocaml
//                 ^^^^^^ keyword.other.method-definition.ocaml
//                        ^^^ entity.name.function.method.ocaml
//                 ^^^^^^^^^^^^ meta.method.ocaml
//          ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.object.ocaml

class foo = object
//          ^^^^^^ meta.object.ocaml
end
//<- meta.object.ocaml

class foo = object
//          ^^^^^^ meta.object.ocaml
  method bar x = x
//^^^^^^^^^^^^ meta.method.ocaml
  method! bar x = x
//^^^^^^^ keyword.other.method-definition.ocaml
//^^^^^^^^^^^^^ meta.method.ocaml
end
//<- meta.object.ocaml
