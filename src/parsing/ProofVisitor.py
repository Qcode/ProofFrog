# Generated from src/antlr/Proof.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ProofParser import ProofParser
else:
    from ProofParser import ProofParser

# This class defines a complete generic visitor for a parse tree produced by ProofParser.

class ProofVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProofParser#program.
    def visitProgram(self, ctx:ProofParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#reduction.
    def visitReduction(self, ctx:ProofParser.ReductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#proof.
    def visitProof(self, ctx:ProofParser.ProofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#lets.
    def visitLets(self, ctx:ProofParser.LetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#assumptions.
    def visitAssumptions(self, ctx:ProofParser.AssumptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#theorem.
    def visitTheorem(self, ctx:ProofParser.TheoremContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameList.
    def visitGameList(self, ctx:ProofParser.GameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameStep.
    def visitGameStep(self, ctx:ProofParser.GameStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#induction.
    def visitInduction(self, ctx:ProofParser.InductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameModule.
    def visitGameModule(self, ctx:ProofParser.GameModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameAdversary.
    def visitGameAdversary(self, ctx:ProofParser.GameAdversaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#concreteGame.
    def visitConcreteGame(self, ctx:ProofParser.ConcreteGameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#game.
    def visitGame(self, ctx:ProofParser.GameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameBody.
    def visitGameBody(self, ctx:ProofParser.GameBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gamePhase.
    def visitGamePhase(self, ctx:ProofParser.GamePhaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gameExport.
    def visitGameExport(self, ctx:ProofParser.GameExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#field.
    def visitField(self, ctx:ProofParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#initializedField.
    def visitInitializedField(self, ctx:ProofParser.InitializedFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#simpleStatement.
    def visitSimpleStatement(self, ctx:ProofParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#statement.
    def visitStatement(self, ctx:ProofParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#lvalue.
    def visitLvalue(self, ctx:ProofParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#methodSignature.
    def visitMethodSignature(self, ctx:ProofParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#paramList.
    def visitParamList(self, ctx:ProofParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#createSetExp.
    def visitCreateSetExp(self, ctx:ProofParser.CreateSetExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#inExp.
    def visitInExp(self, ctx:ProofParser.InExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#andExp.
    def visitAndExp(self, ctx:ProofParser.AndExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#fnCallExp.
    def visitFnCallExp(self, ctx:ProofParser.FnCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#notEqualsExp.
    def visitNotEqualsExp(self, ctx:ProofParser.NotEqualsExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#addExp.
    def visitAddExp(self, ctx:ProofParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#geqExp.
    def visitGeqExp(self, ctx:ProofParser.GeqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#createArrayExp.
    def visitCreateArrayExp(self, ctx:ProofParser.CreateArrayExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#notExp.
    def visitNotExp(self, ctx:ProofParser.NotExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#gtExp.
    def visitGtExp(self, ctx:ProofParser.GtExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#ltExp.
    def visitLtExp(self, ctx:ProofParser.LtExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#subtractExp.
    def visitSubtractExp(self, ctx:ProofParser.SubtractExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#equalsExp.
    def visitEqualsExp(self, ctx:ProofParser.EqualsExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#multiplyExp.
    def visitMultiplyExp(self, ctx:ProofParser.MultiplyExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#subsetsExp.
    def visitSubsetsExp(self, ctx:ProofParser.SubsetsExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#unionExp.
    def visitUnionExp(self, ctx:ProofParser.UnionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#intExp.
    def visitIntExp(self, ctx:ProofParser.IntExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#sizeExp.
    def visitSizeExp(self, ctx:ProofParser.SizeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#typeExp.
    def visitTypeExp(self, ctx:ProofParser.TypeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#concatenateExp.
    def visitConcatenateExp(self, ctx:ProofParser.ConcatenateExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#variableExp.
    def visitVariableExp(self, ctx:ProofParser.VariableExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#leqExp.
    def visitLeqExp(self, ctx:ProofParser.LeqExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#setMinusExp.
    def visitSetMinusExp(self, ctx:ProofParser.SetMinusExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#divideExp.
    def visitDivideExp(self, ctx:ProofParser.DivideExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#binaryNumExp.
    def visitBinaryNumExp(self, ctx:ProofParser.BinaryNumExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#parenExp.
    def visitParenExp(self, ctx:ProofParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#sliceExp.
    def visitSliceExp(self, ctx:ProofParser.SliceExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#arrayAccessExp.
    def visitArrayAccessExp(self, ctx:ProofParser.ArrayAccessExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#argList.
    def visitArgList(self, ctx:ProofParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#variable.
    def visitVariable(self, ctx:ProofParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#arrayType.
    def visitArrayType(self, ctx:ProofParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#intType.
    def visitIntType(self, ctx:ProofParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#lvalueType.
    def visitLvalueType(self, ctx:ProofParser.LvalueTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#optionalType.
    def visitOptionalType(self, ctx:ProofParser.OptionalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#mapType.
    def visitMapType(self, ctx:ProofParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#setType.
    def visitSetType(self, ctx:ProofParser.SetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#bitStringType.
    def visitBitStringType(self, ctx:ProofParser.BitStringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#boolType.
    def visitBoolType(self, ctx:ProofParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#productType.
    def visitProductType(self, ctx:ProofParser.ProductTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#integerExpression.
    def visitIntegerExpression(self, ctx:ProofParser.IntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#bitstring.
    def visitBitstring(self, ctx:ProofParser.BitstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#set.
    def visitSet(self, ctx:ProofParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#moduleImport.
    def visitModuleImport(self, ctx:ProofParser.ModuleImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#methodBody.
    def visitMethodBody(self, ctx:ProofParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProofParser#id.
    def visitId(self, ctx:ProofParser.IdContext):
        return self.visitChildren(ctx)



del ProofParser