pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Code Quality Checks') {
            steps {
                sh 'flake8 .'
            }
        }
        
        stage('Code Coverage') {
            steps {
                sh 'coverage run -m pytest'
                sh 'coverage report'
                sh 'coverage xml'
            }
            post {
                always {
                    junit 'reports/**/*.xml'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, includes: '**/htmlcov/index.html', reportDir: 'htmlcov', reportFiles: 'index.html', reportName: 'Code Coverage'])
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}
