# Generated from MyLanguage.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete listener for a parse tree produced by MyLanguageParser.
class MyLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MyLanguageParser#program.
    def enterProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#program.
    def exitProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#function_list.
    def enterFunction_list(self, ctx:MyLanguageParser.Function_listContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#function_list.
    def exitFunction_list(self, ctx:MyLanguageParser.Function_listContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#function_def.
    def enterFunction_def(self, ctx:MyLanguageParser.Function_defContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#function_def.
    def exitFunction_def(self, ctx:MyLanguageParser.Function_defContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#arguments.
    def enterArguments(self, ctx:MyLanguageParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arguments.
    def exitArguments(self, ctx:MyLanguageParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#argument.
    def enterArgument(self, ctx:MyLanguageParser.ArgumentContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#argument.
    def exitArgument(self, ctx:MyLanguageParser.ArgumentContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#type.
    def enterType(self, ctx:MyLanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#type.
    def exitType(self, ctx:MyLanguageParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#block.
    def enterBlock(self, ctx:MyLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#block.
    def exitBlock(self, ctx:MyLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#statement_list.
    def enterStatement_list(self, ctx:MyLanguageParser.Statement_listContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#statement_list.
    def exitStatement_list(self, ctx:MyLanguageParser.Statement_listContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#statement.
    def enterStatement(self, ctx:MyLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#statement.
    def exitStatement(self, ctx:MyLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#conditionWithElse.
    def enterConditionWithElse(self, ctx:MyLanguageParser.ConditionWithElseContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#conditionWithElse.
    def exitConditionWithElse(self, ctx:MyLanguageParser.ConditionWithElseContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#conditionNoElse.
    def enterConditionNoElse(self, ctx:MyLanguageParser.ConditionNoElseContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#conditionNoElse.
    def exitConditionNoElse(self, ctx:MyLanguageParser.ConditionNoElseContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#loop_stmt.
    def enterLoop_stmt(self, ctx:MyLanguageParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#loop_stmt.
    def exitLoop_stmt(self, ctx:MyLanguageParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#init_stmt.
    def enterInit_stmt(self, ctx:MyLanguageParser.Init_stmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#init_stmt.
    def exitInit_stmt(self, ctx:MyLanguageParser.Init_stmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#post_stmt.
    def enterPost_stmt(self, ctx:MyLanguageParser.Post_stmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#post_stmt.
    def exitPost_stmt(self, ctx:MyLanguageParser.Post_stmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#var_list.
    def enterVar_list(self, ctx:MyLanguageParser.Var_listContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#var_list.
    def exitVar_list(self, ctx:MyLanguageParser.Var_listContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#var.
    def enterVar(self, ctx:MyLanguageParser.VarContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#var.
    def exitVar(self, ctx:MyLanguageParser.VarContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#expression.
    def enterExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#expression.
    def exitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MyLanguageParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MyLanguageParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MyLanguageParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MyLanguageParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MyLanguageParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MyLanguageParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MyLanguageParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MyLanguageParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MyLanguageParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MyLanguageParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MyLanguageParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MyLanguageParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MyLanguageParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MyLanguageParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MyLanguageParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MyLanguageParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#number.
    def enterNumber(self, ctx:MyLanguageParser.NumberContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#number.
    def exitNumber(self, ctx:MyLanguageParser.NumberContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#parameters.
    def enterParameters(self, ctx:MyLanguageParser.ParametersContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#parameters.
    def exitParameters(self, ctx:MyLanguageParser.ParametersContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#empty.
    def enterEmpty(self, ctx:MyLanguageParser.EmptyContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#empty.
    def exitEmpty(self, ctx:MyLanguageParser.EmptyContext):
        pass



del MyLanguageParser