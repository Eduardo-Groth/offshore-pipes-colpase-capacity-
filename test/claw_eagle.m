tic
clc
close all
csvwrite('mesh_size.csv',mesh_size)
csvwrite('P.csv',P)
csvwrite('t_clad.csv',t_clad)
csvwrite('R.csv',R)
csvwrite('f0.csv',f0)
csvwrite('exc.csv',exc)
fid = fopen('folder.txt','wt');
fprintf(fid,'%s',folder);
fclose(fid);
if Graphical_User_Interface == 1;
    script = ' script';
else
    script = ' noGUI';
end
dos(strcat('abaqus cae ',script,'="',main,'\','desert_eagle.py','"'));
cd(folder)
r=0;
for i=1:size(R,2);
    for j=1:size(f0,2);
        for k=1:size(exc,2);
            for l=1:size(t_clad,2);
                r=r+1;
                lpf(i,j,k,l).data(:,:) = importdata([sprintf('%04d',r),'_output.txt']);
                Pc(i,j,k,l) = max(lpf(i,j,k,l).data(:,2));
            end
        end
    end
end
%%
dinfo = dir(folder);
dinfo([dinfo.isdir]) = [];
files = fullfile(folder, {dinfo.name});
delete(files{:})
cd(main)
delete('abaqus1.rec','abaqus_acis.log','just_run_I.asv','abaqus.rpy','Main.asv')
delete('mesh_size.csv','P.csv','R.csv','folder.txt','t_clad.csv','exc.csv','f0.csv')
clc
if save_results == 1
    save('316_L','lpf','Pc')
end
if grafic == 1
    figure
    set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0.04, 1, 0.96]);
    count=0;
    for k=1:size(exc,2);
        for l=1:size(t_clad,2);
            count=count+1;
            if size(exc,2)*size(t_clad,2)>1;
                subplot(round(size(exc,2)*size(t_clad,2)/2),2,count)
            end
            for j=1:size(f0,2);
                hold on
                plot(R,Pc(:,j,k,l),'-o','LineWidth',1.5)
                xlabel('D/t')
                ylabel('Pc Mpa')
                axis([7.5 30 0 150])
                title(['ecc ',sprintf('%g',exc(k)),'  t_{clad}  ',sprintf('%g',t_clad(l))],'fontsize',9)
            end
        end
    end
end
clc
if txt == 1
    for k=1:size(exc,2)
        for l=1:size(t_clad,2)
            for j=1:size(f0,2)
                fprintf('\n')
                fprintf('clad thickness %g\n',t_clad(l))
                fprintf('eccentricity %g\n',exc(k))
                fprintf('ovalization %g\n', f0(j))
                fprintf('\n')
                fprintf('%g\n',Pc(:,j,k,l))
                fprintf('\n')
            end
        end
    end
end
toc

