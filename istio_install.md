# istio install config
istioctl install -f istio/ingress-egress-iop.yaml
kubectl label namespace rezz-dev istio-injection=enabled
