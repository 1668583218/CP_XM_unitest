pipeline{
	agent any
    stages{
        stage("test"){
        	steps{
        	bat '''
        	        cd report
                    del *.html
                    cd ..
        	        cd scripts
                    python run_html.py
                    cd ..
                    cd report
                    ren *.html 1.html
                    '''


        	}
        }
}
    post {
    always {
    // One or more steps need to be included within each condition's block.
    emailext attachmentsPattern:
        'report/1.html',
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