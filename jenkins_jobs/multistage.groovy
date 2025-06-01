def sharedVar = 'sharedVar'

pipeline {
    agent any
    
    options {
        ansiColor('xterm')  // Поддержка цветов (требует плагин AnsiColor)
    }

    environment {
        GLOBAL_VAR = 'initial'
    }
    stages {
        stage('get token') {
            steps {
                script {
                    echo "stage 1 Переменная GLOBAL_VAR до изменения ${env.GLOBAL_VAR}"
                    echo "stage 1 Переменная sharedVar до изменения ${sharedVar}"
                    env.GLOBAL_VAR = 'changed in Stage 1'
                    sharedVar = 'changed Data from Stage 1'
                }
            }
        }
        stage('use token') {
            when {
                not {
                    environment name: 'GLOBAL_VAR', value: 'initial'
                }
            }
            steps {
                script {
                    echo "Значение env.GLOBAL_VAR: ${env.GLOBAL_VAR}"
                    echo "Значение GLOBAL_VAR: ${GLOBAL_VAR}"
                    echo "Значение sharedVar: ${sharedVar}"
                }
            }
        }
    }
}
