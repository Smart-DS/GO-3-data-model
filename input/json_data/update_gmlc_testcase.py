import json
import os

schema_path = '../../datamodel/schemas/input_data_file_schema.json'

data_path = 'PSY_RTS_GMLC_data_fixed_load_commit.json'

output_path = 'PSY_RTS_GMLC_data_fixed_load_commit_v2.json'
missing_path = 'PSY_RTS_GMLC_data_fixed_load_commit_missing.json' #elements that were not included in the data file
extra_path = 'PSY_RTS_GMLC_data_fixed_load_commit_extra.json' #elements that were included in the data file but shouldn't have been

all_missing_data = {}
all_extra_data = {}


def get_objects(element,element_name,schema):
    properties = schema['definitions'][element]['properties']
    network_elements = []
    for prop in properties.values():
        name = prop['title']
        the_type = ''
        if 'type' in prop and prop['type'] == 'array':
            the_type = 'array'
            the_class = prop['items']['$ref'].split('/')[-1]
        else:
            the_type = 'object'
            the_class = prop['allOf'][0]['$ref'].split('/')[-1]
        network_elements.append((name,the_type,the_class))
    return network_elements

def get_attributes(element,element_name,network_element,schema,data):
    if 'required' in schema['definitions'][network_element[2]]:
        required = schema['definitions'][network_element[2]]['required']
        all_values = schema['definitions'][network_element[2]]['properties'].keys()

        missing = set()
        extra = set()
        for component in required:
            do_recurse = True
            component_type = None
            if 'type' in schema['definitions'][network_element[2]]['properties'][component] :
                component_type = schema['definitions'][network_element[2]]['properties'][component]['type']
                do_recurse = False

            if network_element[1] == 'array':
                if not network_element[0] in data and network_element[1] == 'array':
                    data[network_element[0]] = []
                    all_missing_data[network_element[2]] = []
                for entry in data[network_element[0]]:
                    if do_recurse:
                        the_class = schema['definitions'][network_element[2]]['properties'][component]['allOf'][0]['$ref'].split('/')[-1]
                        validate_elements([(the_class,component)],schema,entry,False)

                    else:
                        if not component in element:
                            if component_type == 'number':
                                entry[component] = 0.0
                            if component_type == 'integer':
                                entry[component] = 0
                            if component_type == 'boolean':
                                entry[component] = 0
                            if component_type == 'string':
                                entry[component] = ""
                            if component_type == 'array':
                                entry[component] = []
                            missing.add(component)
                        for component2 in entry:
                            if not component2 in all_values:
                                extra.add(component2)
                        for component2 in extra:
                            if component2 in entry:
                                entry.pop(component2)

            else:
                if do_recurse:
                    the_class = schema['definitions'][network_element[2]]['properties'][component]['allOf'][0]['$ref'].split('/')[-1]
                    validate_elements([(the_class,component)],schema,data[network_element[0]],False)
                else:
                    if not component in data[network_element[0]]:
                        if component_type == 'number':
                            data[network_element[0]][component] = 0.0
                        if component_type == 'boolean':
                            data[network_element[0]][component] = 0
                        if component_type == 'integer':
                            data[network_element[0]][component] = 0
                        if component_type == 'string':
                            data[network_element[0]][component] = ""
                        if component_type == 'array':
                            data[network_element[0]][component] = []
                        missing.add(component)
                    for component2 in data[network_element[0]]:
                        if not component2 in all_values:
                            extra.add(component2)
                    for component2 in extra:
                        if component2 in data[network_element[0]]:
                            data[network_element[0]].pop(component2)

        if len(missing) > 0 or len(extra) >0:
            all_missing_data[network_element[2]] = list(missing)
            all_extra_data[network_element[2]] = list(extra)
           # print(element_name)
           # print('missing',missing)
           # print('extra',extra)
    else:
        pass
        #print(network_element[0], 'has nothing required')

def validate_elements(element_list,schema,data,is_object):
    for element,element_name in element_list:
        if not is_object:
            network_element = (element_list[0][1],'object',element_list[0][0])
            get_attributes(element,element_name,network_element,schema,data)
        else:
            network_elements = get_objects(element,element_name,schema)
            for network_element in network_elements:
                get_attributes(element,element_name,network_element,schema,data[element_name])



with open(schema_path) as schema_fp:
    schema = json.load(schema_fp)
    with open(data_path) as data_fp:
        data = json.load(data_fp)
        element_list = [('Network','network'),('TimeSeriesInput','time_series_input')]
        validate_elements(element_list,schema, data,True)
        with open(output_path,'w') as output_fp:
            json.dump(data,output_fp,indent=4)

        with open(missing_path,'w') as missing_fp:
            json.dump(all_missing_data,missing_fp,indent=4)
        with open(extra_path,'w') as extra_fp:
            json.dump(all_extra_data,extra_fp,indent=4)

