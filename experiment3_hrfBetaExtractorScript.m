%% Extracts beta values for HbO only and stores as .csv

%get filelist, only gets .mat files (containing betas)
filelist = dir('*.mat')
filelist = {filelist.name}

for i = filelist

    %Generates filename variable, removes .mat, adds .csv
    nom = split(i, '.')  %separates .mat
    nom = nom(1)         %take only name
    nom = strcat(nom, '.csv')  %add .csv
    nom = char(nom) %convert to char vector
    
    %loads data from filelist
    load(char(i))

    %gets beta HbO2 cell
    bcell = output.misc.beta{1}

    %gets array of beta values
    betas = squeeze(bcell(1,1,:,:))

    %saves to file with name
    csvwrite(nom, betas)

    clear output
    clear bcell
    clear betas
    clear nom
     
end




