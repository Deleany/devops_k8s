pipeline {
    agent any 

    environment{
        GLOBAL_VAR = ''
        SOME_VAR = 1

    }
    stages{
        stage('get token'){
            steps {
                script{
                    env.GLOBAL_VAR == 'Hello from Stage 1'
                }
            }
        stage('use token'){
            steps {
                script{
                    println(env.GLOBAL_VAR)
                    println(env.SOME_VAR)
                }
            }

        }
             
    }
}
