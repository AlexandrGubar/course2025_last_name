pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Simulating compilation on Windows..."
                bat 'python -m py_compile main.py'
            }
        }
        stage('Define Variant') {
            steps {
                echo "Variant 4 detected from repository."
            }
        }
        stage('Form report') {
            steps {
                echo "Preparing HTML report template..."
            }
        }
        stage('Test') {
            steps {
                echo "Running automated tests..."
                bat 'python test.py'
            }
        }
    }
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
        }
    }
}
