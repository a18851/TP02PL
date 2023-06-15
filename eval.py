# arith_eval

class AEval:
    symbols = {}

    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "seq": lambda args: args[-1],
        "atr": lambda args: AEval._attrib(args),
        "esc": lambda args: print(args[0]),
    }

    @staticmethod
    def _attrib(args):  # A:=10   {'op':'atr'  args: [ "A", 10 ]}
        value = args[1]
        AEval.symbols[args[0]] = value
        return None

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return AEval._eval_operator(ast)
        if type(ast) is str:
            return ast
        raise Exception(f"Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = [AEval.evaluate(a) for a in ast['args']]
            if op in AEval.operators:
                func = AEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            varid = ast["var"]
            if varid in AEval.symbols:
                return AEval.symbols[varid]
            raise Exception(f"error: '{varid}' undeclared (first use in this function)")

        raise Exception('Undefined AST')

