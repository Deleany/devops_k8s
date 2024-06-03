# istio install config
istioctl install --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY --set profile=minimal
istioctl install -f istio/ingress.yaml
istioctl install -f istio/egress.yaml
