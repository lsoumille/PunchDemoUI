punchplatform_ip = "192.168.1.91"

ssh_port = 22

env_variables = "export PATH='/home/adm-infra/punchplatform-standalone-3.3.5/bin':$PATH && export PUNCHPLATFORM_CONF_DIR='/home/adm-infra/punchplatform-standalone-3.3.5/conf' && export PUNCHPLATFORM_LOG_DIR='/home/adm-infra/punchplatform-standalone-3.3.5/logs' && export TERM='xterm' &&"

kibana = "http://" + punchplatform_ip + ":5601"

grafana = "http://" + punchplatform_ip + ":3000"

punch_admin = "http://" + punchplatform_ip + ":5000"

storm_ui = "http://" + punchplatform_ip + ":8080"

elastic = "http://" + punchplatform_ip + ":9200"

elastic_indices = "http://" + punchplatform_ip + ":9200/_cat/indices"

tenant = "mytenant"

account = "adm-infra"

password = "azerty"

noise_path = "/home/adm-infra/punchplatform-standalone-3.3.5/conf/resources/injector/demo/noise/launchNoise.sh"