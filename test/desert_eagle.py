
from abaqus import *  
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import os
import string 
import numpy as np
import displayGroupOdbToolset as dgo
import connectorBehavior
import csv

f = open("folder.txt")
folder = f.read()
with open('mesh_size.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        mesh_size=float(row[0])    
    
with open('P.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        P=float(row[0])

t_clad=[]
with open('t_clad.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):   
            t_clad.append(float(row[i]))

R=[]
with open('R.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):   
            R.append(float(row[i]))
            
f0=[]
with open('f0.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):   
            f0.append(float(row[i]))

exc=[]
with open('exc.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(len(row)):   
            exc.append(float(row[i]))

count=0
for j in range(len(R)):
    for jj in range(len(f0)):
        for jjj in range(len(exc)):
            for jjjj in range(len(t_clad)):
                ##################################################
                ##################################################
                modelo = mdb.models['Model-1']
                s = modelo.ConstrainedSketch(name='__profile__', sheetSize=0.5)
                g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
                raio_maior = 0.3048/2
                D=raio_maior*2
                delta=f0[jj]*D/2
                D_max=D+delta
                D_min=D-delta   
                t_bs=D/R[j] 
                dt=(exc[jjj]*t_bs)/2 
                t1=((D_max/2)-t_bs+dt)+t_clad[jjjj]
                t2=((D_min/2)-t_bs)+t_clad[jjjj] 
                s.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(D_max/2, 0.0), axisPoint2=(0.0, D_min/2))
                s.EllipseByCenterPerimeter(center=(dt, 0.0), axisPoint1=((D_max/2)-t_bs+dt, 0.0), axisPoint2=(0.0, (D_min/2)-t_bs))
                modelo.Part(name='Part-1', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
                p = mdb.models['Model-1'].parts['Part-1']
                p.BaseShell(sketch=s) 
                modelo.Material(name='X six five')
                material1 = modelo.materials['X six five']
                material1.Density(table=((7860.0, ), ))
                material1.Elastic(table=((207e9, 0.3), ))
                material1.Plastic(table=((450e6, 0.0), 
                             (454500000, 6.88732E-05),
                             (459045000, 0.000144614),
                             (463635450, 0.000228164),
                             (468271804.5, 0.000320595),
                             (472954522.5, 0.000423131),
                             (477684067.8, 0.00053717),
                             (482460908.4, 0.000664303),
                             (487285517.5, 0.00080635),
                             (492158372.7, 0.000965384),
                             (497079956.4, 0.001143771),
                             (502050756, 0.001344211),
                             (507071263.6, 0.001569784),
                             (512141976.2, 0.001824006),
                             (517263396, 0.002110887),
                             (522436029.9, 0.002435002),
                             (527660390.2, 0.002801573),
                             (532936994.1, 0.003216558),
                             (538266364.1, 0.003686755),
                             (543649027.7, 0.00421992),
                             (549085518, 0.004824905),
                             (554576373.2, 0.005511808),
                             (560122136.9, 0.006292155),
                             (565723358.3, 0.007179095),
                             (571380591.8, 0.008187633),
                             (577094397.8, 0.00933489),
                             (582865341.7, 0.010640404),
                             (588693995.2, 0.012126468),
                             (594580935.1, 0.013818522),
                             (600526744.5, 0.015745592),
                             (606532011.9, 0.017940802),
                             (612597332, 0.020441949),
                             (618723305.3, 0.02329216),
                             (624910538.4, 0.02654065),
                             (631159643.8, 0.030243576),
                             (637471240.2, 0.03446502),
                             (643845952.6, 0.039278103),
                             (650284412.1, 0.044766264),
                             (656787256.3, 0.051024716),
                             (663355128.8, 0.058162102),
                             (669988680.1, 0.0663024),
                             (676688566.9, 0.075587074),
                             (683455452.6, 0.086177552),
                             (690290007.1, 0.098258038),
                             (697192907.2, 0.112038727),
                             (704164836.3, 0.127759468),
                             (711206484.6, 0.145693957),
                             (718318549.5, 0.166154504),
                             (725501735, 0.189497485),
                             (732756752.3, 0.216129561),
                             (740084319.8, 0.24651477),)) 
                modelo.Material(name='inox three hundred and sixteen L')
                material2 = modelo.materials['inox three hundred and sixteen L']
                material2.Density(table=((7860.0, ), ))
                material2.Elastic(table=((193e9, 0.3), ))
                material2.Plastic(table=((205000000, 0),
                             (207050000, 0.000121803),
                             (209120500, 0.000247451),
                             (211211705, 0.000377064),
                             (213323822.1, 0.000510767),
                             (215457060.3, 0.00064869),
                             (217611630.9, 0.000790966),
                             (219787747.2, 0.000937732),
                             (221985624.7, 0.00108913),
                             (224205480.9, 0.001245306),
                             (226447535.7, 0.001406411),
                             (228712011.1, 0.0015726),
                             (230999131.2, 0.001744034),
                             (233309122.5, 0.001920879),
                             (235642213.7, 0.002103304),
                             (237998635.9, 0.002291487),
                             (240378622.2, 0.002485609),
                             (242782408.4, 0.002685857),
                             (245210232.5, 0.002892425),
                             (247662334.8, 0.003105513),
                             (250138958.2, 0.003325325),
                             (252640347.8, 0.003552074),
                             (255166751.2, 0.00378598),
                             (257718418.8, 0.004027267),
                             (260295602.9, 0.00427617),
                             (262898559, 0.004532927),
                             (265527544.6, 0.004797788),
                             (268182820, 0.005071008),
                             (270864648.2, 0.00535285),
                             (273573294.7, 0.005643587),
                             (276309027.6, 0.0059435),
                             (279072117.9, 0.006252878),
                             (281862839.1, 0.00657202),
                             (284681467.5, 0.006901234),
                             (287528282.2, 0.007240837),
                             (290403565, 0.007591159),
                             (293307600.6, 0.007952536),
                             (296240676.6, 0.008325318),
                             (299203083.4, 0.008709865),
                             (302195114.2, 0.009106549),
                             (305217065.4, 0.009515751),
                             (308269236, 0.009937868),
                             (311351928.4, 0.010373306),
                             (314465447.7, 0.010822487),
                             (317610102.2, 0.011285844),
                             (320786203.2, 0.011763824),
                             (323994065.2, 0.012256889),
                             (327234005.9, 0.012765515),
                             (330506345.9, 0.013290193),
                             (333811409.4, 0.01383143),
                             (337149523.5, 0.014389747),
                             (340521018.7, 0.014965686),
                             (343926228.9, 0.0155598),
                             (347365491.2, 0.016172665),
                             (350839146.1, 0.016804871),
                             (354347537.6, 0.017457029),
                             (357891012.9, 0.018129769),
                             (361469923.1, 0.018823741),
                             (365084622.3, 0.019539614),
                             (368735468.5, 0.02027808),
                             (372422823.2, 0.021039852),
                             (376147051.4, 0.021825664),
                             (379908522, 0.022636277),
                             (383707607.2, 0.023472472),
                             (387544683.2, 0.024335057),
                             (391420130.1, 0.025224865),
                             (395334331.4, 0.026142755),
                             (399287674.7, 0.027089614),
                             (403280551.4, 0.028066354),
                             (407313357, 0.029073921),
                             (411386490.5, 0.030113285),
                             (415500355.4, 0.031185452),
                             (419655359, 0.032291456),
                             (423851912.6, 0.033432365),
                             (428090431.7, 0.03460928),
                             (432371336, 0.035823338),
                             (436695049.4, 0.037075712),
                             (441061999.9, 0.03836761),
                             (445472619.9, 0.03970028),
                             (449927346.1, 0.041075008),
                             (454426619.5, 0.042493122),
                             (458970885.7, 0.043955991),
                             (463560594.6, 0.045465028),
                             (468196200.5, 0.04702169),
                             (472878162.5, 0.048627479),
                             (477606944.2, 0.050283946),
                             (482383013.6, 0.05199269),
                             (487206843.7, 0.053755362),
                             (492078912.2, 0.055573663),
                             (496999701.3, 0.057449349),
                             (501969698.3, 0.059384231),
                             (506989395.3, 0.061380177),
                             (512059289.2, 0.063439114),
                             (517179882.1, 0.06556303),
                             (522351681, 0.067753976),
                             (527575197.8, 0.070014068),
                             (532850949.7, 0.072345487),
                             (538179459.2, 0.074750485),
                             (543561253.8, 0.077231384),
                             (548996866.4, 0.079790579),
                             (554486835, 0.082430541),
                             (560031703.4, 0.085153819),
                             (565632020.4, 0.087963042),
                             (571288340.6, 0.090860924),
                             (577001224, 0.093850262), 
                             (582771236.3, 0.096933941),
                             (588598948.6, 0.100114941),
                             (594484938.1, 0.103396332),
                             (600429787.5, 0.106781282),
                             (606434085.4, 0.110273059),
                             (612498426.2, 0.113875036),
                             (618623410.5, 0.11759069),
                             (624809644.6, 0.121423608),
                             (631057741, 0.125377492),
                             (637368318.4, 0.129456158),
                             (643742001.6, 0.133663546),
                             (650179421.6, 0.138003717),
                             (656681215.9, 0.142480862),
                             (663248028, 0.147099304),
                             (669880508.3, 0.151863503),
                             (676579313.4, 0.156778057),
                             (683345106.5, 0.161847713),
                             (690178557.6, 0.167077365),
                             (697080343.2, 0.172472063),
                             (704051146.6, 0.178037015),
                             (711091658.1, 0.183777595),
                             (718202574.6, 0.189699345),
                             (725384600.4, 0.195807984),
                             (732638446.4, 0.202109408),
                             (739964830.9, 0.208609703),
                             (747364479.2, 0.215315145),
                             (754838124, 0.222232207),
                             (762386505.2, 0.22936757),
                             (770010370.2, 0.236728121),
                             (777710473.9, 0.244320969),
                             (785487578.7, 0.252153444),
                             (793342454.5, 0.260233108),
                             (801275879, 0.268567764),
                             (809288637.8, 0.277165458),
                             (817381524.2, 0.286034491),
                             (825555339.4, 0.295183428),
                             (833810892.8, 0.304621102),
                             (842149001.8, 0.314356624),))                
                modelo.HomogeneousSolidSection(name='Section-1', material='X six five', thickness=None)
                modelo.HomogeneousSolidSection(name='Section-2', material='inox three hundred and sixteen L', thickness=None) 
                f, e, d1 = p.faces, p.edges, p.datums
                t = p.MakeSketchTransform(sketchPlane=p.faces[0], sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0))                 
                s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.71, gridSpacing=0.01, transform=t)                          
                g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
                s.setPrimaryObject(option=SUPERIMPOSE)
                p = mdb.models['Model-1'].parts['Part-1']
                p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
                s.EllipseByCenterPerimeter(center=(dt, 0.0), axisPoint1=(t1, 0.0),axisPoint2=(0.0, t2))                 
                p.PartitionFaceBySketch(faces=p.faces[0], sketch=s)   
                pickedRegions = (p.faces[0],)  
                p.SectionAssignment(region=pickedRegions, sectionName='Section-1', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)   
                pickedRegions = (p.faces[1],)    
                p.SectionAssignment(region=pickedRegions, sectionName='Section-2', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
                lista=[]
                for i in range(len(p.faces)):
                    lista.append(p.faces[i])
            
                pickedRegions = tuple(lista)
                p.setMeshControls(regions=pickedRegions, elemShape=QUAD, algorithm=MEDIAL_AXIS)
                p.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)
                p.generateMesh()  
                q = modelo.rootAssembly
                q.Instance(name = "Duto",part = p, dependent = ON)   
                a = q.instances['Duto']
                modelo.StaticRiksStep(name='riks', previous='Initial', nlgeom=ON)
                load_edges = a.edges[0:1]
                region = q.Surface(side1Edges=load_edges, name='Surf-1')   
                modelo.Pressure(name='Load-1', createStepName='riks', region=region, distributionType=UNIFORM, field='', magnitude=P)  
                factor = np.arange(1,0,-0.01) 
                nodes_list = [None]*len(factor) 
                
                n = p.nodes 
                for i in range(len(factor)):
                    nodes_list[i] = n.getByBoundingSphere((0+0.001*mesh_size,-(D_min/2),0),factor[i]*mesh_size)         
                    if len(nodes_list[i])==1: 
                       nodes_ok = nodes_list[i]
                       break
        
                p.Set(nodes=nodes_ok, name='Node-Set')         
                region = a.sets['Node-Set']    
                mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='riks', region=region, u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)                     
                
                jobname = "Job_dt_%s_f_%s_e_%s_t_%s" % (R[j],f0[jj],exc[jjj],t_clad[jjjj]) 
        
                def change_name(J):
                   B = J.split(".")
                   S = "_".join(B)
                   return S
                jobname = change_name(jobname)
                mdb.Job(name=jobname, model='Model-1', description='', type=ANALYSIS, 
                    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
                    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
                    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
                    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
                    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)

                path= folder
                os.chdir(path)
                mdb.jobs[jobname].submit(consistencyChecking=OFF, datacheckJob=False)
                mdb.jobs[jobname].waitForCompletion()

                ##################################################
                ##################################################
                
                os.chdir(path)
                count = count+1              
                
                jobname = "Job_dt_%s_f_%s_e_%s_t_%s" %(R[j],f0[jj],exc[jjj],t_clad[jjjj])                
                
                def change_name(J):
                   B = J.split(".")
                   S = "_".join(B)
                   return S               
                
                jobname = change_name(jobname)                
                
                session.mdbData.summary() 
                
                o1 = session.openOdb(name=jobname+'.odb')
                odb = session.odbs[jobname+'.odb']                
                
                xyList = session.XYDataFromHistory(odb=odb, name='List', outputVariableName='Load proportionality factor: LPF for Whole Model', steps=('riks', ), ) 
                
                output_file = '%04d_output.txt' %(count)
                
                fp = open(output_file,'w+')
                for i in range(len(xyList)):
                    fp.write('%.9f %.9f\n' % (xyList[i][0],xyList[i][1]))
                fp.close()
    
    
    






