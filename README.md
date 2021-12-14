# DashAppExample
## Dash examples to test features

### Pattern-Matching features for callbacks
  1. Index will be set as dictionary with keys shown below: 
     - id={'type': .. , 'id': .., 'specifier': ..} 
        - where type can be either 'input', 'multiinput' and 'container' and much 
           more, \
        - whereas specifier can be either 'visibility', 'disabled', 'activate' and 
           much more depending on the user specification 
       
### *Type*
  - 'input' = any single input in a row that will produce single output or 
    multiple inputs in a row but produce same number of outputs
  - 'multiinput' = multiple inputs in a row that will produce multiple outputs*
    - 2 row inputs will produce a single output (output requires a list)
      - (Exchange Current Density = [anode-vol_ex_cd, cathode-vol_ex_cd]
    - 4 row inputs will produce two outputs (each outputs require a list)
      - BPP Thermal-Conductivity 
        - output anode bpp = [anode-bpp-z, anode-bpp-x]
        - output cathode bpp = [cathode-bpp-z, cathode-bpp-x]
  - 'container' = callbacks will affect the container that holds the 
    component; further specified under 'Specifier'
        
### *Specifier*
- 'visibility' = component affected can be set whether it will be visible or not
- 'disabled' = value of a disabled component cannot be changed and user will 
  have no access to the component
- 'activate' = checklist, activated when True ([1]), False ([ ]); for df.
  row_input, keyword arguments (widget='checklist', activated=True) to set 
  checklist to True
   
   


