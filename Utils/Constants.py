punchplatform_ip = "192.168.1.91"

env_variables = "export PATH='/home/adm-infra/punchplatform-standalone-3.3.5/bin':$PATH && export PUNCHPLATFORM_CONF_DIR='/home/adm-infra/punchplatform-standalone-3.3.5/conf' && export PUNCHPLATFORM_LOG_DIR='/home/adm-infra/punchplatform-standalone-3.3.5/logs' && export TERM='xterm' &&"

kibana = "http://" + punchplatform_ip + ":5601"

grafana = "http://" + punchplatform_ip + ":3000"

punch_admin = "http://" + punchplatform_ip + ":5000"

storm_ui = "http://" + punchplatform_ip + ":8080"