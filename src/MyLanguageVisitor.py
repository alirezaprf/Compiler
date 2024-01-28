# Generated from MyLanguage.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MyLanguageParser.

class MyLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLanguageParser#program.
    def visitProgram(self, ctx:MyLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#function_list.
    def visitFunction_list(self, ctx:MyLanguageParser.Function_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#function_def.
    def visitFunction_def(self, ctx:MyLanguageParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arguments.
    def visitArguments(self, ctx:MyLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#argument.
    def visitArgument(self, ctx:MyLanguageParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#type.
    def visitType(self, ctx:MyLanguageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#block.
    def visitBlock(self, ctx:MyLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#statement_list.
    def visitStatement_list(self, ctx:MyLanguageParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#statement.
    def visitStatement(self, ctx:MyLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#conditionWithElse.
    def visitConditionWithElse(self, ctx:MyLanguageParser.ConditionWithElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#conditionNoElse.
    def visitConditionNoElse(self, ctx:MyLanguageParser.ConditionNoElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#loop_stmt.
    def visitLoop_stmt(self, ctx:MyLanguageParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#init_stmt.
    def visitInit_stmt(self, ctx:MyLanguageParser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#post_stmt.
    def visitPost_stmt(self, ctx:MyLanguageParser.Post_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#var_list.
    def visitVar_list(self, ctx:MyLanguageParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#var.
    def visitVar(self, ctx:MyLanguageParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#expression.
    def visitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:MyLanguageParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:MyLanguageParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#equalityExpression.
    def visitEqualityExpression(self, ctx:MyLanguageParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#relationalExpression.
    def visitRelationalExpression(self, ctx:MyLanguageParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MyLanguageParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MyLanguageParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MyLanguageParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MyLanguageParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#number.
    def visitNumber(self, ctx:MyLanguageParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#parameters.
    def visitParameters(self, ctx:MyLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#empty.
    def visitEmpty(self, ctx:MyLanguageParser.EmptyContext):
        return self.visitChildren(ctx)



del MyLanguageParser