### cAdvisor launching
1. Create the monitor network
```bash
docker network create monitor
```
2. Run cAdvisor container
```bash
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --network=monitor \
  gcr.io/cadvisor/cadvisor:latest
```
3. cAdvisor is now available at `localhost:8080`
### Prometheus launching
1. Write the prometheus.yml config file (already written)
2. Run Prometheus container (change /path/to/prometheus.yml to the path to your Prometheus config file)
```bash
docker run -d \
  -p 9090:9090 \
  --name=prometheus \
  -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
  --network monitor \
  prom/prometheus
```
3. Prometheus is now available at `localhost:9090`
### Grafana launching
1. Run Grafana container
```bash
docker run -d -p 3000:3000 --name=grafana --network=monitor grafana/grafana
```
2. Grafana is now available at `localhost:3000`
3. Enter default credentials (admin/admin)
4. Add Prometheus as a data source
- Go to "Connections" tab 
- "View configured data sources"
- "Add data source" > "Prometheus" 
- Enter address of Prometheus container (`http://prometheus:9090`)
5. Make a dashboard
- Go to "Dashboards" tab
- Click "Create dashboard"
- "Add visualisation"
- Select "prometheus" as data source
- Choose some metric in the "Metric" field
- Save the dashboard
