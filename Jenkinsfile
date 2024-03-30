pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from version control
                git 'https://github.com/garapati33/pythontest.git'
            }
        }
        stage('Install dependencies') {
            steps {
                // Install pytest
                sh 'pip install pytest'
            }
        }
        stage('Run tests') {
            steps {
                // Run your Python tests
                sh 'pytest test_math_utils.py'
            }
        }
    }
}
