pipeline {
    agent any 

    envirinment{
        GLOBAL_VAR = ''
        SOME_VAR = 1

    }
    stages{
        stage ('get token'){

            script{
                env.GLOBAL_VAR == 'Hello from Stage 1'
            }

        stage('user token'){
            script{
                println(env.GLOBAL_VAR)
                println(env.SOME_VAR)
            }
        }
        }
        
    }
    
}
