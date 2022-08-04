pipeline{
	agent any
    stages{
        stage("test"){
        	steps{
        	bat '''cd scripts
                    python run_html.py'''
        	}
        }
}
    post {
    always {
    // One or more steps need to be included within each condition's block.
    emailext
        attachmentsPattern:
            'report/*.html',
        body:
            '''<html>
                <h1>${TEST_COUNTS,var="pass"}</h1>
                </html>''',
        subject:
            'pipeline 测试邮件发送',
        to:
            '1668583218@qq.com'
  }
}
}