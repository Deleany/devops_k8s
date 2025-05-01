for ns in $(kubectl get ns | tail -n +2 | awk '{print $1}');
do kubectl get pod -n $ns | grep -v Running | tail -n +2 | awk '{print $1}' | xargs kubectl delete pod -n $ns;
done
