%% riks 2d rotine colapse MCP
% Equinor Lamef Collapse Project
% This routine was development to parametric study of collpase in clad pipes MCP. 
% general coments: 
% external diamenter: 12". materials: backing steel in x65 clad in inox 316 L
% if happpens all right at the end of the run teh folder of .odb file is clear
% and the folder main stay with desert_eagle.py, Main.m and claw_eagle.m files 
% the name of the abaqus job are convenently chosen with information dt, f0,ecc an thickness of clad
% developer contact eduardo.groth@ufrgs.br
%% INSTRUCTIONS
%  put the files (desert_eagle.py; Maim.m, claw_eagle.m) on the same folder
%  created a folder for results (may be into the folder above)
%  set parameter below, the parametric lists can be "any" size
%  caution! the parameters must be feasible
%% general options
save_results=0;              % 1 for save the resultas at .mat file. anyother to no save
Graphical_User_Interface=0;  % 1 for open Abaqus GUI. To end the processes it need close manually
grafic = 1;                  % 1 for plot all the results at the same grafic
txt =1;                      % 1 for show the pressure of colaspe calculated on matlab promp
%% paths 
main='C:\Users\Groth\Desktop\dnv_clads\test';           % this folder should contain the files 
folder='C:\Users\Groth\Desktop\dnv_clads\test\results'; % this folder the .odb are save during the process
%% FEM options 
mesh_size=1e-3;       % quad side size of element. CPS4R plane stress
P=1e6;                % apllied pressure set 
%% PARAMETRICS PARAMETERS
R=[7.5,10,15,20,30];      % d/t radio. external diameter and total thickness t_bs+t_clad
f0=[0.0025]%,0.005,0.01,0.02,0.03,0.04];  % ovalization. D minimal in vertical
exc=[0]%,0.05,0.1,0.25];    % eccentricity. aplied on x+ (horizontal positive direction) 
t_clad=[3e-3]%,5.5e-3,7e-3];       % inox 316_L clad thickness 
%%
claw_eagle
fprintf('clad pipe collapse project');
