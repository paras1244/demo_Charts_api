{
	"info": {
		"_postman_id": "b0edfe14-434e-4e32-8012-023be6ab8870",
		"name": "Glib_test",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "19442321"
	},
	"item": [
		{
			"name": "User Register / Login",
			"item": [
				{
					"name": "token",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"username\" : \"Ajit\",\n    \"password\" : \"password123#\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/token/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"token",
								""
							]
						}
					},
					"response": [
						{
							"name": "token",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"username\" : \"paras\",\n    \"password\" : \"password123#\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/token/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"token",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sat, 27 Aug 2022 10:10:12 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "483"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTY4MTQxMiwiaWF0IjoxNjYxNTk1MDEyLCJqdGkiOiI3NDE1NmM5MzYyNTY0MDI1ODA1OWJiMWUyYjI5OTY4NiIsInVzZXJfaWQiOjF9.3TXdidnOs34CihjEuuSmmFgkY-ul0INfMrGFF21HFjA\",\n    \"access\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNTk1MzEyLCJpYXQiOjE2NjE1OTUwMTIsImp0aSI6ImM1ODlkMWMzMTM5NDQ3NDM4OTYyOWFkYzhlNTI5YzBlIiwidXNlcl9pZCI6MX0.917qVTDXofD0ZuF-Kb2Hp673vQMWQPvw8_yzUK3NdGk\"\n}"
						},
						{
							"name": "token",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"username\" : \"tom2\",\n    \"password\" : \"password123#\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/token/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"token",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sun, 28 Aug 2022 18:15:38 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "483"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"refresh\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTc5NjkzOCwiaWF0IjoxNjYxNzEwNTM4LCJqdGkiOiIzMGU2YThmMTA5ZTY0MWM4OTk4MzE3M2FjZmYyNjA4NSIsInVzZXJfaWQiOjd9.8FsqxEIoEOUOlsqltCtCNQGwHeF6Gky9v4gU6H70IAY\",\n    \"access\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzExNDM4LCJpYXQiOjE2NjE3MTA1MzgsImp0aSI6IjAzOGU4ODQ3YmI4YjQzNGViMDNlYmFjMzhhODcwOTYxIiwidXNlcl9pZCI6N30.ch9NVkerTL0vYrcy04g4_VsjRpMV7xn3gRF0h-0_3CA\"\n}"
						}
					]
				},
				{
					"name": "Register USer",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"username\": \"tom2\",\n    \"email\": \"tom2@email.com\",\n    \"first_name\": \"tom2\",\n    \"last_name\": \"white\",\n    \"password\": \"password123#\",\n    \"password2\": \"password123#\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/register/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"register",
								""
							]
						}
					},
					"response": [
						{
							"name": "Register USer",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"username\": \"Ajit\",\n    \"email\": \"ajit@email.com\",\n    \"first_name\": \"ajit\",\n    \"last_name\": \"maurya\",\n    \"password\": \"password123#\",\n    \"password2\": \"password123#\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/register/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"register",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sat, 27 Aug 2022 10:12:59 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "85"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"username\": \"Ajit\",\n    \"email\": \"ajit@email.com\",\n    \"first_name\": \"ajit\",\n    \"last_name\": \"maurya\"\n}"
						},
						{
							"name": "Register USer",
							"originalRequest": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"username\": \"tom2\",\n    \"email\": \"tom2@email.com\",\n    \"first_name\": \"tom2\",\n    \"last_name\": \"white\",\n    \"password\": \"password123#\",\n    \"password2\": \"password123#\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/register/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"register",
										""
									]
								}
							},
							"status": "Created",
							"code": 201,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sun, 28 Aug 2022 18:14:58 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "POST, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "91"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 7,\n    \"username\": \"tom2\",\n    \"email\": \"tom2@email.com\",\n    \"first_name\": \"tom2\",\n    \"last_name\": \"white\"\n}"
						}
					]
				},
				{
					"name": "Get Logdin user details",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzExNDM4LCJpYXQiOjE2NjE3MTA1MzgsImp0aSI6IjAzOGU4ODQ3YmI4YjQzNGViMDNlYmFjMzhhODcwOTYxIiwidXNlcl9pZCI6N30.ch9NVkerTL0vYrcy04g4_VsjRpMV7xn3gRF0h-0_3CA",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/get-details/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"get-details",
								""
							]
						}
					},
					"response": [
						{
							"name": "get logdin User Details",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/get-details/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"get-details",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sat, 27 Aug 2022 10:18:55 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "67"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 2,\n    \"first_name\": \"ajit\",\n    \"last_name\": \"maurya\",\n    \"username\": \"Ajit\"\n}"
						},
						{
							"name": "Get Logdin user details",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/get-details/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"get-details",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sun, 28 Aug 2022 18:15:58 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "66"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "{\n    \"id\": 7,\n    \"first_name\": \"tom2\",\n    \"last_name\": \"white\",\n    \"username\": \"tom2\"\n}"
						}
					]
				}
			]
		},
		{
			"name": "Complaint",
			"item": [
				{
					"name": "Admin (Worker)",
					"item": [
						{
							"name": "Worker Review Complaint",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzExNTU0LCJpYXQiOjE2NjE3MTA2NTQsImp0aSI6ImY3ZDE4Y2U5NDhmZjQwODc4MmRmNzZjZTUzODVmZTQ0IiwidXNlcl9pZCI6Mn0.dxEChiWA8jaK8OGzxFgPdqjYUVbba_z6r8wI5fg00dc",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"complaint_id\" : \"1\",\n    \"complaint_status\" : \"PROGRESS\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"admin-review-complaint",
										""
									]
								}
							},
							"response": [
								{
									"name": "Worker Review Complaint - COMPLETED",
									"originalRequest": {
										"method": "PUT",
										"header": [],
										"body": {
											"mode": "raw",
											"raw": "{\n    \"complaint_id\" : \"1\",\n    \"complaint_status\" : \"COMPLETED\"\n}",
											"options": {
												"raw": {
													"language": "json"
												}
											}
										},
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"admin-review-complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 11:30:31 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, PUT, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "205"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "{\n    \"id\": 1,\n    \"subject\": \"complaint-Subject1\",\n    \"description\": \"complaint-description-1\",\n    \"user\": 1,\n    \"complaint_status\": \"COMPLETED\",\n    \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n    \"updated_at\": \"2022-08-27T11:30:31.012647Z\"\n}"
								},
								{
									"name": "Worker Review Complaint - PROGRESS",
									"originalRequest": {
										"method": "PUT",
										"header": [],
										"body": {
											"mode": "raw",
											"raw": "{\n    \"complaint_id\" : \"1\",\n    \"complaint_status\" : \"PROGRESS\"\n}",
											"options": {
												"raw": {
													"language": "json"
												}
											}
										},
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"admin-review-complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 11:32:17 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, PUT, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "204"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "{\n    \"id\": 1,\n    \"subject\": \"complaint-Subject1\",\n    \"description\": \"complaint-description-1\",\n    \"user\": 1,\n    \"complaint_status\": \"PROGRESS\",\n    \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n    \"updated_at\": \"2022-08-27T11:32:17.418673Z\"\n}"
								}
							]
						},
						{
							"name": "List all Complaints",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzExNTU0LCJpYXQiOjE2NjE3MTA2NTQsImp0aSI6ImY3ZDE4Y2U5NDhmZjQwODc4MmRmNzZjZTUzODVmZTQ0IiwidXNlcl9pZCI6Mn0.dxEChiWA8jaK8OGzxFgPdqjYUVbba_z6r8wI5fg00dc",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"admin-review-complaint",
										""
									]
								}
							},
							"response": [
								{
									"name": "List all Complaints",
									"originalRequest": {
										"method": "GET",
										"header": [],
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"admin-review-complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 11:38:41 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, PUT, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "206"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "[\n    {\n        \"id\": 1,\n        \"subject\": \"complaint-Subject1\",\n        \"description\": \"complaint-description-1\",\n        \"user\": 1,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n        \"updated_at\": \"2022-08-27T11:32:17.418673Z\"\n    }\n]"
								},
								{
									"name": "List all Complaints",
									"originalRequest": {
										"method": "GET",
										"header": [],
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/admin-review-complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"admin-review-complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sun, 28 Aug 2022 18:18:32 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, PUT, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "2715"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "[\n    {\n        \"id\": 1,\n        \"subject\": \"complaint-Subject1\",\n        \"description\": \"complaint-description-1\",\n        \"user\": 1,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n        \"updated_at\": \"2022-08-28T18:17:45.430822Z\"\n    },\n    {\n        \"id\": 2,\n        \"subject\": \"tom-complaint-Subject1\",\n        \"description\": \"tom-complaint-description-1\",\n        \"user\": 6,\n        \"complaint_status\": \"COMPLETED\",\n        \"created_at\": \"2022-08-27T12:04:37.359163Z\",\n        \"updated_at\": \"2022-08-28T16:54:50.368504Z\"\n    },\n    {\n        \"id\": 3,\n        \"subject\": \"tom-complaint-Subject2\",\n        \"description\": \"tom-complaint-description-2\",\n        \"user\": 6,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:05:46.454657Z\",\n        \"updated_at\": \"2022-08-27T12:05:46.454688Z\"\n    },\n    {\n        \"id\": 4,\n        \"subject\": \"tom-complaint-3\",\n        \"description\": \"tom-complaint-description-3\",\n        \"user\": 6,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:05:59.235834Z\",\n        \"updated_at\": \"2022-08-27T12:05:59.235900Z\"\n    },\n    {\n        \"id\": 5,\n        \"subject\": \"tom-complaint-4\",\n        \"description\": \"tom-complaint-description-4\",\n        \"user\": 6,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:06:05.754760Z\",\n        \"updated_at\": \"2022-08-27T12:06:05.754796Z\"\n    },\n    {\n        \"id\": 6,\n        \"subject\": \"jack-complaint-1\",\n        \"description\": \"jack-complaint-description-1\",\n        \"user\": 4,\n        \"complaint_status\": \"COMPLETED\",\n        \"created_at\": \"2022-08-27T12:07:09.231517Z\",\n        \"updated_at\": \"2022-08-28T17:01:31.454953Z\"\n    },\n    {\n        \"id\": 7,\n        \"subject\": \"jack-complaint-2\",\n        \"description\": \"jack-complaint-description-2\",\n        \"user\": 4,\n        \"complaint_status\": \"COMPLETED\",\n        \"created_at\": \"2022-08-27T12:07:21.652415Z\",\n        \"updated_at\": \"2022-08-28T17:01:35.635465Z\"\n    },\n    {\n        \"id\": 8,\n        \"subject\": \"jack-complaint-3\",\n        \"description\": \"jack-complaint-description-3\",\n        \"user\": 4,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:07:30.041847Z\",\n        \"updated_at\": \"2022-08-27T12:07:30.041873Z\"\n    },\n    {\n        \"id\": 9,\n        \"subject\": \"jack-complaint-4\",\n        \"description\": \"jack-complaint-description-4\",\n        \"user\": 4,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:07:54.263044Z\",\n        \"updated_at\": \"2022-08-27T12:07:54.263070Z\"\n    },\n    {\n        \"id\": 10,\n        \"subject\": \"john-complaint-1\",\n        \"description\": \"john-complaint-description-1\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:01.227200Z\",\n        \"updated_at\": \"2022-08-27T12:09:01.227230Z\"\n    },\n    {\n        \"id\": 11,\n        \"subject\": \"john-complaint-2\",\n        \"description\": \"john-complaint-description-2\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:10.125427Z\",\n        \"updated_at\": \"2022-08-27T12:09:10.125457Z\"\n    },\n    {\n        \"id\": 12,\n        \"subject\": \"john-complaint-3\",\n        \"description\": \"john-complaint-description-3\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:16.906812Z\",\n        \"updated_at\": \"2022-08-27T12:09:16.906842Z\"\n    },\n    {\n        \"id\": 13,\n        \"subject\": \"john-complaint-4\",\n        \"description\": \"john-complaint-description-4\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:22.818924Z\",\n        \"updated_at\": \"2022-08-27T12:09:22.818944Z\"\n    }\n]"
								}
							]
						}
					]
				},
				{
					"name": "User",
					"item": [
						{
							"name": "create Complaint-1",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjAyNDA0LCJpYXQiOjE2NjE2MDIxMDQsImp0aSI6ImNkYjY0OWZkYTg3MjQyMjE4YThhYWQ5YjVhYjQwOWFkIiwidXNlcl9pZCI6NX0.rnl2TIl7Gu6eevJEWkwot7DHFPvXIgdCvz6usguCsdQ",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"subject\" : \"john-complaint-4\",\n    \"description\" : \"john-complaint-description-4\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/complaint/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"complaint",
										""
									]
								}
							},
							"response": [
								{
									"name": "Complain-1",
									"originalRequest": {
										"method": "POST",
										"header": [],
										"body": {
											"mode": "raw",
											"raw": "{\n    \"subject\" : \"complaint-Subject1\",\n    \"description\" : \"complaint-description-1\"\n}",
											"options": {
												"raw": {
													"language": "json"
												}
											}
										},
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 11:09:16 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, POST, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "204"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "{\n    \"id\": 1,\n    \"subject\": \"complaint-Subject1\",\n    \"description\": \"complaint-description-1\",\n    \"user\": 1,\n    \"complaint_status\": \"PROGRESS\",\n    \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n    \"updated_at\": \"2022-08-27T11:09:15.997833Z\"\n}"
								},
								{
									"name": "tom create Complaint-1",
									"originalRequest": {
										"method": "POST",
										"header": [],
										"body": {
											"mode": "raw",
											"raw": "{\n    \"subject\" : \"tom-complaint-Subject1\",\n    \"description\" : \"tom-complaint-description-1\"\n}",
											"options": {
												"raw": {
													"language": "json"
												}
											}
										},
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 12:04:37 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, POST, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "212"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "{\n    \"id\": 2,\n    \"subject\": \"tom-complaint-Subject1\",\n    \"description\": \"tom-complaint-description-1\",\n    \"user\": 6,\n    \"complaint_status\": \"PROGRESS\",\n    \"created_at\": \"2022-08-27T12:04:37.359163Z\",\n    \"updated_at\": \"2022-08-27T12:04:37.359193Z\"\n}"
								},
								{
									"name": "Error Uniq Together",
									"originalRequest": {
										"method": "POST",
										"header": [],
										"body": {
											"mode": "raw",
											"raw": "{\n    \"subject\" : \"tom-complaint-Subject1\",\n    \"description\" : \"tom-complaint-description-1\"\n}",
											"options": {
												"raw": {
													"language": "json"
												}
											}
										},
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 12:04:56 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, POST, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "91"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "{\n    \"non_field_errors\": [\n        \"The fields user, subject, complaint_status must make a unique set.\"\n    ]\n}"
								}
							]
						},
						{
							"name": "Get Complaint of logged in user",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzEzNjc2LCJpYXQiOjE2NjE3MTI3NzYsImp0aSI6IjJjYzJkZWUzNjVlYzQ2NWI5OTg4YzA1MjJlZjE3ZjU1IiwidXNlcl9pZCI6MX0.7_KkTP0czKqhmitJubIB4fcDiY01NCYB1KU4lCL93rw",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/complaint/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"complaint",
										""
									]
								}
							},
							"response": [
								{
									"name": "Get Complaint of logged in user",
									"originalRequest": {
										"method": "GET",
										"header": [],
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sat, 27 Aug 2022 11:15:22 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, POST, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "206"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "[\n    {\n        \"id\": 1,\n        \"subject\": \"complaint-Subject1\",\n        \"description\": \"complaint-description-1\",\n        \"user\": 1,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T11:09:15.997788Z\",\n        \"updated_at\": \"2022-08-27T11:09:15.997833Z\"\n    }\n]"
								},
								{
									"name": "Get Complaint of logged in user",
									"originalRequest": {
										"method": "GET",
										"header": [],
										"url": {
											"raw": "http://127.0.0.1:8000/complaint/complaint/",
											"protocol": "http",
											"host": [
												"127",
												"0",
												"0",
												"1"
											],
											"port": "8000",
											"path": [
												"complaint",
												"complaint",
												""
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Sun, 28 Aug 2022 17:50:28 GMT"
										},
										{
											"key": "Server",
											"value": "WSGIServer/0.2 CPython/3.8.10"
										},
										{
											"key": "Content-Type",
											"value": "application/json"
										},
										{
											"key": "Vary",
											"value": "Accept"
										},
										{
											"key": "Allow",
											"value": "GET, POST, HEAD, OPTIONS"
										},
										{
											"key": "X-Frame-Options",
											"value": "DENY"
										},
										{
											"key": "Content-Length",
											"value": "837"
										},
										{
											"key": "X-Content-Type-Options",
											"value": "nosniff"
										},
										{
											"key": "Referrer-Policy",
											"value": "same-origin"
										},
										{
											"key": "Cross-Origin-Opener-Policy",
											"value": "same-origin"
										}
									],
									"cookie": [],
									"body": "[\n    {\n        \"id\": 10,\n        \"subject\": \"john-complaint-1\",\n        \"description\": \"john-complaint-description-1\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:01.227200Z\",\n        \"updated_at\": \"2022-08-27T12:09:01.227230Z\"\n    },\n    {\n        \"id\": 11,\n        \"subject\": \"john-complaint-2\",\n        \"description\": \"john-complaint-description-2\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:10.125427Z\",\n        \"updated_at\": \"2022-08-27T12:09:10.125457Z\"\n    },\n    {\n        \"id\": 12,\n        \"subject\": \"john-complaint-3\",\n        \"description\": \"john-complaint-description-3\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:16.906812Z\",\n        \"updated_at\": \"2022-08-27T12:09:16.906842Z\"\n    },\n    {\n        \"id\": 13,\n        \"subject\": \"john-complaint-4\",\n        \"description\": \"john-complaint-description-4\",\n        \"user\": 5,\n        \"complaint_status\": \"PROGRESS\",\n        \"created_at\": \"2022-08-27T12:09:22.818924Z\",\n        \"updated_at\": \"2022-08-27T12:09:22.818944Z\"\n    }\n]"
								}
							]
						}
					]
				}
			]
		},
		{
			"name": "Charts API",
			"item": [
				{
					"name": "user Complaints with solve %",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/complaint/chart/user-complaint-count/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"complaint",
								"chart",
								"user-complaint-count",
								""
							]
						}
					},
					"response": [
						{
							"name": "user Complaints with solve %",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/chart/user-complaint-count/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"chart",
										"user-complaint-count",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sun, 28 Aug 2022 16:56:17 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "164"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[\n    {\n        \"user\": 1,\n        \"count\": 1,\n        \"solved_count\": 100\n    },\n    {\n        \"user\": 4,\n        \"count\": 4,\n        \"solved_count\": 0\n    },\n    {\n        \"user\": 5,\n        \"count\": 4,\n        \"solved_count\": 0\n    },\n    {\n        \"user\": 6,\n        \"count\": 4,\n        \"solved_count\": 25\n    }\n]"
						}
					]
				},
				{
					"name": "Total Complaints",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/complaint/chart/all-complaint/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"complaint",
								"chart",
								"all-complaint",
								""
							]
						}
					},
					"response": [
						{
							"name": "total Complaints",
							"originalRequest": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/complaint/chart/all-complaint/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"complaint",
										"chart",
										"all-complaint",
										""
									]
								}
							},
							"status": "OK",
							"code": 200,
							"_postman_previewlanguage": "json",
							"header": [
								{
									"key": "Date",
									"value": "Sun, 28 Aug 2022 17:19:45 GMT"
								},
								{
									"key": "Server",
									"value": "WSGIServer/0.2 CPython/3.8.10"
								},
								{
									"key": "Content-Type",
									"value": "application/json"
								},
								{
									"key": "Vary",
									"value": "Accept"
								},
								{
									"key": "Allow",
									"value": "GET, HEAD, OPTIONS"
								},
								{
									"key": "X-Frame-Options",
									"value": "DENY"
								},
								{
									"key": "Content-Length",
									"value": "115"
								},
								{
									"key": "X-Content-Type-Options",
									"value": "nosniff"
								},
								{
									"key": "Referrer-Policy",
									"value": "same-origin"
								},
								{
									"key": "Cross-Origin-Opener-Policy",
									"value": "same-origin"
								}
							],
							"cookie": [],
							"body": "[\n    {\n        \"total_complaints\": 13,\n        \"in_progress\": 9,\n        \"completed\": 4,\n        \"solved_percantage\": 30.77,\n        \"solved_percantage_str\": \"30.77 %\"\n    }\n]"
						}
					]
				}
			]
		}
	]
}