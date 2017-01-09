// SYNTAX TEST "source.ocaml"
(* test *)
// ^ comment.block.ocaml
fun x -> y
// <- keyword.other.function-definition.ocaml
// <- meta.function.anonymous.definition.ocaml
//^^^^^^ meta.function.anonymous.definition.ocaml
//  ^ variable.parameter.ocaml
//    ^^ keyword.other.anonymous-function-arrow.ocaml
//      ^^ !meta.function.anonymous.definition.ocaml
begin fun x -> y end
// <- keyword.control.begin-end.ocaml
//    ^^^^^^^^ meta.function.anonymous.definition.ocaml
//    ^^^ meta.function.anonymous.definition.ocaml
//        ^ variable.parameter.ocaml
//          ^^ keyword.other.anonymous-function-arrow.ocaml
//             ^^^^^ !meta.function.anonymous.definition.ocaml
//               ^^^ keyword.control.begin-end.ocaml
   a>>=b
//  ^^^ entity.name.function.infix.ocaml
   a!=b
//  ^^ keyword.operator.infix.symbol.ocaml
   a=b
//  ^ keyword.operator.infix.symbol.ocaml
   a<>b
//  ^^ keyword.operator.infix.symbol.ocaml
   a>b
//  ^ keyword.operator.infix.symbol.ocaml
   a<b
//  ^ keyword.operator.infix.symbol.ocaml
   a->b
//  ^^ punctuation.separator.function-return.ocaml
   a->>b
//  ^^^ entity.name.function.infix.ocaml
   a+.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a-.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a/.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a*.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a+b
//  ^ keyword.operator.infix.integer.ocaml
   a-b
//  ^ keyword.operator.infix.integer.ocaml
   a/b
//  ^ keyword.operator.infix.integer.ocaml
   a*b
//  ^ keyword.operator.infix.integer.ocaml
   a|>b
//  ^^ entity.name.function.infix.ocaml
val test: a -> b
// <- keyword.other.ocaml
//  ^^^^ entity.name.type.value-signature.ocaml
//      ^ punctuation.separator.type-constraint.ocaml
//        ^ storage.type.ocaml
//          ^^ punctuation.separator.function-return.ocaml
//             ^ storage.type.ocaml
val ( >> ): a -> b
// <- keyword.other.ocaml
//  ^^^^^^ entity.name.type.value-signature.ocaml
//        ^ punctuation.separator.type-constraint.ocaml
//          ^ storage.type.ocaml
//            ^^ punctuation.separator.function-return.ocaml
//               ^ storage.type.ocaml
