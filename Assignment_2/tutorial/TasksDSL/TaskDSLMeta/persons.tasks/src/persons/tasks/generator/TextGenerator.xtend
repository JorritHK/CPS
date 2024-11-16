package persons.tasks.generator

import persons.tasks.taskDSL.BinaryBooleanOperator
import persons.tasks.taskDSL.BooleanExpressionBracket
import persons.tasks.taskDSL.BooleanExpressionConstant
import persons.tasks.taskDSL.CompareOperator
import persons.tasks.taskDSL.ExpressionAddition
import persons.tasks.taskDSL.ExpressionBalance
import persons.tasks.taskDSL.ExpressionBinOp
import persons.tasks.taskDSL.ExpressionBracket
import persons.tasks.taskDSL.ExpressionCompOp
import persons.tasks.taskDSL.ExpressionConstantInt
import persons.tasks.taskDSL.ExpressionDivision
import persons.tasks.taskDSL.ExpressionMaximum
import persons.tasks.taskDSL.ExpressionMinimum
import persons.tasks.taskDSL.ExpressionMinus
import persons.tasks.taskDSL.ExpressionModulo
import persons.tasks.taskDSL.ExpressionMultiply
import persons.tasks.taskDSL.ExpressionPlus
import persons.tasks.taskDSL.ExpressionPower
import persons.tasks.taskDSL.ExpressionSubtraction
import persons.tasks.taskDSL.LunchAction
import persons.tasks.taskDSL.MeetingAction
import persons.tasks.taskDSL.NotExpression
import persons.tasks.taskDSL.PaperAction
import persons.tasks.taskDSL.PaymentAction
import persons.tasks.taskDSL.Planning
import persons.tasks.taskDSL.Task
import persons.tasks.taskDSL.TimeUnit

class TextGenerator {
	def static toText(Planning root)'''
		Info of the planning «root.name»
		All Persons:«"\n"»
		«FOR p : root.persons»«"\t"»«p.name»«"\n"»«ENDFOR»
		All actions of tasks:
		«FOR t : root.tasks BEFORE "====== \n"
SEPARATOR "\n&\n" AFTER "====="»
		«action2Text(t.action)»«infoAction(t)»
		«ENDFOR»
		Other way of listing all tasks:
		«FOR a: Auxiliary.getActions(root) SEPARATOR " , " »
		«action2Text(a)»
		«ENDFOR»'''
		
	def static dispatch action2Text(LunchAction action)'''
		Lunch at location «action.location»'''
		
	def static dispatch action2Text(MeetingAction action)'''
		Meeting with topic «action.topic»'''
		
	def static dispatch action2Text(PaperAction action)'''
		Paper for journal «action.report»'''
		
	def static dispatch action2Text(PaymentAction action)'''
		«IF action.condition !== null»if «generateExpression(action.condition)»
		then «ENDIF»Pay «generateExpression(action.amount)» euro'''
		
	def static infoAction(Task t)'''
		«IF t.duration !== null» with duration: «t.duration.dl»«ENDIF»'''
		
	def static CharSequence toText(TimeUnit u){
		switch(u){
		case TimeUnit::MINUTE: return '''m'''
		case TimeUnit::HOUR: return '''h'''
		case TimeUnit::DAY: return '''d'''
		case TimeUnit::WEEK: return '''w'''
		}
	}
	
	def static dispatch CharSequence generateExpression(ExpressionAddition expr)
		'''(«generateExpression(expr.left)» + «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionSubtraction expr)
		'''(«generateExpression(expr.left)» - «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionMultiply expr)
		'''(«generateExpression(expr.left)» * «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionDivision expr)
		'''(«generateExpression(expr.left)» / «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionMaximum expr)
		'''max(«generateExpression(expr.left)», «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionMinimum expr)
		'''min(«generateExpression(expr.left)», «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionModulo expr)'''
		(fmod(«generateExpression(expr.left)», «generateExpression(expr.right)») >=
		0 ? fmod(«generateExpression(expr.left)», «generateExpression(expr.right)») :
		fmod(«generateExpression(expr.left)», «generateExpression(expr.right)») +
		«generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionPower expr)
		'''pow(«generateExpression(expr.left)», «generateExpression(expr.right)»)'''
	def static dispatch CharSequence generateExpression(ExpressionMinus expr)
		'''(-«generateExpression(expr.sub)»)'''
	def static dispatch CharSequence generateExpression(ExpressionPlus expr)
		'''(+«generateExpression(expr.sub)»)'''
	def static dispatch CharSequence generateExpression(ExpressionBracket expr)
		'''(«generateExpression(expr.sub)») '''
	def static dispatch CharSequence generateExpression(ExpressionConstantInt expr)
		'''«expr.value»'''
	def static dispatch CharSequence generateExpression(ExpressionBalance expr)
		'''«expr.value»'''
	
	def static dispatch CharSequence generateExpression(ExpressionBinOp expr)
		'''(«generateExpression(expr.left)» «genBinOp(expr.bop)»
		«generateExpression(expr.right)»)'''

	def static CharSequence genBinOp(BinaryBooleanOperator op){
		switch(op){
			case BinaryBooleanOperator::AND: return '''AND'''
			case BinaryBooleanOperator::OR: return '''OR'''
		}
	}
	
	def static dispatch CharSequence generateExpression(ExpressionCompOp expr)
		'''(«generateExpression(expr.left)» «genCompOp(expr.op)»
		«generateExpression(expr.right)»)'''
		
	def static CharSequence genCompOp(CompareOperator op){
		switch(op){
			case CompareOperator::EQ: return '''='''
			case CompareOperator::NEQ: return '''!='''
			case CompareOperator::GEQ: return '''>='''
			case CompareOperator::G: return '''>'''
			case CompareOperator::LEQ: return '''<='''
			case CompareOperator::L: return '''<'''
		}
	}
	def static dispatch CharSequence generateExpression(BooleanExpressionBracket expr)
		'''(«generateExpression(expr.sub)»)'''
	def static dispatch CharSequence generateExpression(NotExpression expr)
		'''NOT («generateExpression(expr.sub)»)'''
	def static dispatch CharSequence generateExpression(BooleanExpressionConstant expr)
		'''«expr.value»''' // use literal
	
	
}