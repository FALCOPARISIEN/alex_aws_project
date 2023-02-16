Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@FALCOPARISIEN 
raoufcherfa
/
employe
Public
Fork your own copy of raoufcherfa/employe
Code
Issues
Pull requests
Actions
Projects
Security
Insights
employe/Jenkinsfile

Abderaouf CHERFA add deploys
Latest commit 9c3d1cd 13 hours ago
 History
 0 contributors
39 lines (39 sloc)  978 Bytes

pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/raoufcherfa/employe.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest unit_tests.py'
            }
        }
        stage('Run API') {
            steps {
                sh 'python app.py &'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout Dev && git merge origin/master'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'echo "http://localhost:5000"'
            }
        }
    }
}
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
employe/Jenkinsfile at master · raoufcherfa/employe