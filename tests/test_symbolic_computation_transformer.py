import pytest
from proof_frog import visitors, frog_parser, frog_ast
from sympy import symbols


@pytest.mark.parametrize(
    "method,expected,symbol_map",
    [
        # Simple substitution
        (
            """
        void f() {
            Int x = lambda + lambda;
        }
        """,
            """
        void f() {
            Int x = 2 * lambda;
        }
        """,
            {"lambda": symbols("lambda")},
        ),
        (
            """
        BitString<lambda + lambda + 2 * lambda> f(BitString<lambda * 2> x, BitString<lambda + lambda> y) {
            return x || y;
        }
        """,
            """
        BitString<4 * lambda> f(BitString<2 * lambda> x, BitString<2 * lambda> y) {
            return x || y;
        }
        """,
            {"lambda": symbols("lambda")},
        ),
        (
            """
        void f() {
            return 3 + 5;
        }
        """,
            """
        void f() {
            return 8;
        }
        """,
            {},
        ),
    ],
)
def test_symbolic_computation_transformer(
    method: str,
    expected: str,
    symbol_map: dict[(str, symbols)],
) -> None:
    game_ast = frog_parser.parse_method(method)
    expected_ast = frog_parser.parse_method(expected)

    transformed_ast = visitors.SymbolicComputationTransformer(symbol_map).transform(
        game_ast
    )
    print(transformed_ast)
    assert transformed_ast == expected_ast
