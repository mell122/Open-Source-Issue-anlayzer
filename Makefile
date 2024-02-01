# up: build and run the data plane docker
up:
	cd /data
	docker build -t data-plane:latest .
	docker run -v /home/milx/Documents/side-projects/open-source-AI/output:/app/output data-plane:latest
