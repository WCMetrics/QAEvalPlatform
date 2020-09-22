#!/usr/bin/env python3
##
## 2020 (c) almo
## WCMetrics Reordering cuantitative data
## Apache 2.0
## 

components_catalog = ["Google+","Twitter","Facebook","Pinterest","Financial","Weather","Traffic"]
metrics_catalog = ["Size","Ciclomatic","Dependencies","Completeness","Latency","Refress"]

def reord_metrics(data,index):
    component = {
        "Size":data[index+5],
        "Ciclomatic":data[index+2],
        "Dependencies":data[index+3],
        "Completeness":data[index+1],
        "Latency":data[index],
        "Refress":data[index+4]
    }
    return component

def save_component(component):
    response=""
    for metrics in metrics_catalog:
        response += str(component[metrics])+ " "

    return response

def save_experiment(experiment):
    scenario = experiment["Scenario"]
    response = experiment["Response"]
    for component in components_catalog:
        print( save_component(scenario[component])+ response[component])

if __name__ == '__main__':
    with open("/Users/almo/Downloads/CuantitativeAnalysis.txt",'r') as fd_in:
        line = str(fd_in.readline())
        index=1
        while (len(line)>0):
            print("Experimento:" + str(index))
            data = line.split(',')

            scenario = {
                "Google+":reord_metrics(data,18),
                "Twitter":reord_metrics(data,0),
                "Facebook":reord_metrics(data,6),
                "Pinterest":reord_metrics(data,12),
                "Financial":reord_metrics(data,36),
                "Weather":reord_metrics(data,30),
                "Traffic":reord_metrics(data,24),
            }
            #print(scenario)
        
            i=42
            response = {
                "Google+":data[i],
                "Twitter":data[i+2],
                "Facebook":data[i+1],
                "Pinterest":data[i+3],
                "Financial":data[i+4],
                "Weather":data[i+5],
                "Traffic":data[i+6].rstrip('\n'),
            }

            #print(response)

            experiment ={
                "Scenario":scenario,
                "Response":response
            }

            save_experiment(experiment)
            print("\n\n")
            index=index+1
            line = str(fd_in.readline())