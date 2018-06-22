// SYNTAX TEST "source.ocaml"
type t = [%foo]
//       ^^^^^^ meta.extension.algebraic.ocaml
//         ^^^ support.variable.extension.ocaml

type t =
  | X
  | [%foo]
//  ^^^^^^ meta.extension.algebraic.ocaml
//    ^^^ support.variable.extension.ocaml

let t = [%foo]
//      ^^^^^^ meta.extension.algebraic.ocaml
//        ^^^ support.variable.extension.ocaml

module Foo = [%foo]
//           ^^^^^^ meta.extension.algebraic.ocaml
//             ^^^ support.variable.extension.ocaml

module type Foo : [%foo]
//                ^^^^^^ meta.extension.algebraic.ocaml
//                  ^^^ support.variable.extension.ocaml

module type Foo : sig
  [%%foo]
//^^^^^^^ meta.extension.module.ocaml
//   ^^^ support.variable.extension.ocaml
end

module Foo = struct
  [%%foo]
//^^^^^^^ meta.extension.module.ocaml
//   ^^^ support.variable.extension.ocaml
end

class foo = [%foo]
//          ^^^^^^ meta.extension.algebraic.ocaml
//            ^^^ support.variable.extension.ocaml

class foo = object
  [%%foo]
//^^^^^^^ meta.extension.module.ocaml
//   ^^^ support.variable.extension.ocaml
end
