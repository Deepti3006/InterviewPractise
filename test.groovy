import hudson.model.*
import jenkins.model.*
import hudson.model.ParametersAction
import hudson.model.StringParameterValue
def name = build.buildVariableResolver.resolve("NAME")
def age = build.buildVariableResolver.resolve("AGE")
def class1 = build.buildVariableResolver.resolve("CLASS")
def grade = build.buildVariableResolver.resolve("GRADE")
println "NAME=$name"
println "AGE=$age"
println "CLASS=$class1"
println "GRADE=$grade"
def params = [
      new StringParameterValue('NAME', name),
     new StringParameterValue('AGE', age),
      new StringParameterValue('CLASS', class1),
      new StringParameterValue('GRADE', grade),
    ]
def currentBuild = Thread.currentThread().executable
def job = hudson.model.Hudson.instance.getJob("test_endnode")
def paramsActions = new ParametersAction(params)
def cause = new hudson.model.Cause.UpstreamCause(currentBuild)
def causeAction = new hudson.model.CauseAction(cause)
def waitingItem = hudson.model.Hudson.instance.queue.schedule(job, 10, causeAction, paramsActions)
def childFuture = waitingItem.getFuture()
def childBuild = childFuture.get()

