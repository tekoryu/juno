#  │ Vulnerability Name │ Seve… │ CWE Co… │ B… │ S… │ Location             
───┼────────────────────┼───────┼─────────┼────┼────┼────────────────────  
1  │ SQL Injection      │ CRITI │ CWE-89  │ ✓  │ ✓  │ sqli/dao/student.p   
   │                    │ CAL   │         │    │    │ y:42-45              
2  │ Session Fixation   │ HIGH  │ N/A     │ ✗  │ ✗  │ sqli/views.py:42,    
   │                    │       │         │    │    │ sqli/middlewares.p   
   │                    │       │         │    │    │ y:20                 
3  │ Stored Cross-Site  │ HIGH  │ CWE-79  │ ✗  │ ✓  │ sqli/app.py:35,      
   │ Scripting (XSS)    │       │         │    │    │ sqli/views.py:121-   
   │                    │       │         │    │    │ 129                  
4  │ Weak Password      │ HIGH  │ CWE-327 │ ✓  │ ✓  │ sqli/dao/user.py:4   
   │ Hashing (MD5)      │       │         │    │    │ 1                    
5  │ Cross-Site Request │ HIGH  │ N/A     │ ✗  │ ✗  │ sqli/app.py:27       
   │ Forgery (CSRF)     │       │         │    │    │                      
6  │ Missing            │ MEDIU │ N/A     │ ✗  │ ✗  │ Multiple endpoints   
   │ Authorization      │ M     │         │    │    │                      
   │ Checks             │       │         │    │    │                      
7  │ No Rate Limiting   │ MEDIU │ N/A     │ ✗  │ ✗  │ sqli/views.py:33-    
   │                    │ M     │         │    │    │ 45                   
8  │ Debug Mode Enabled │ LOW   │ N/A     │ ✗  │ ✗  │ sqli/app.py:24       
9  │ Docker Security    │ LOW   │ CWE-732 │ ✗  │ ✓  │ docker-              
   │ Misconfigurations  │       │         │    │    │ compose.yml:11       
10 │ Regular Expression │ LOW   │ CWE-    │ ✗  │ ✓  │ sqli/static/js/mat   
   │ DoS (ReDoS)        │       │ 1333    │    │    │ erialize.js:565      
11 │ Insecure Format    │ INFO  │ CWE-134 │ ✗  │ ✓  │ sqli/static/js/mat   
   │ Strings            │       │         │    │    │ erialize.js:645,66   
   │                    │       │         │    │    │ 1,699              
