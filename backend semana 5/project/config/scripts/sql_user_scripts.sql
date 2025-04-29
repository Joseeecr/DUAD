CREATE TABLE lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    date_of_birth DATE NOT NULL,
status_account VARCHAR(50) NOT NULL CHECK (status_account IN ('Currently renting', Currently not renting, Delinquent))
);

insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Tristam McRuvie', 'tmcruvie0@phpbb.com', 'tmcruvie0', 'xG4{u!gDm', '22/04/1979', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Fowler Kubu', 'fkubu1@shareasale.com', 'fkubu1', 'aR0,VBIOOvFL**', '07/05/1981', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Vincenty Batram', 'vbatram2@printfriendly.com', 'vbatram2', 'iF3\DoPl}A4=R', '02/02/1979', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Ravid Nowland', 'rnowland3@drupal.org', 'rnowland3', 'dP2)=|9zlWBjj', '06/09/1964', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Barnett Startin', 'bstartin4@t.co', 'bstartin4', 'vQ4&jy#pF52F', '22/09/1986', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Christoph Dowdell', 'cdowdell5@cpanel.net', 'cdowdell5', 'jB1&+zdj65z', '08/07/1970', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Donaugh Dunphy', 'ddunphy6@live.com', 'ddunphy6', 'wU7#IsEC}*)6', '28/11/2001', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Inger Cowthart', 'icowthart7@cnbc.com', 'icowthart7', 'rS8/>f0Q', '24/09/1976', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Ludovika Schultze', 'lschultze8@ameblo.jp', 'lschultze8', 'yE9$96Dr>S|4,XbJ', '13/07/1973', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Althea Doerling', 'adoerling9@flickr.com', 'adoerling9', 'zI5`\?AGRV', '07/02/1972', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Lillis Carnachen', 'lcarnachena@nsw.gov.au', 'lcarnachena', 'qA1$v*#dc?I%', '05/08/1975', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Henrieta Lattey', 'hlatteyb@topsy.com', 'hlatteyb', 'cT2#`_wCdiI', '06/02/1990', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Leelah Seneschal', 'lseneschalc@ameblo.jp', 'lseneschalc', 'gT3<b%UjK', '06/06/1961', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Jdavie Bullon', 'jbullond@cpanel.net', 'jbullond', 'fV0.|?|`2%7', '02/04/2001', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Bart Feakins', 'bfeakinse@hubpages.com', 'bfeakinse', 'iL3$xR?~"', '27/05/1960', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Katee Schulz', 'kschulzf@yellowbook.com', 'kschulzf', 'nU5/~"(}/1C', '30/11/1977', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Dalli Whyard', 'dwhyardg@feedburner.com', 'dwhyardg', 'yT4"M'',Mc7ll', '07/07/1960', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Worthy Linnane', 'wlinnaneh@e-recht24.de', 'wlinnaneh', 'eQ3!<F%QdS3C', '19/02/2004', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Eugenia Caslin', 'ecaslini@moonfruit.com', 'ecaslini', 'zC8=_,Xq@*v', '08/04/1971', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Virgina Tackley', 'vtackleyj@ebay.co.uk', 'vtackleyj', 'hW0{vN?E', '20/09/1976', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Araldo Aberdeen', 'aaberdeenk@theglobeandmail.com', 'aaberdeenk', 'lE3{PTDy1Z7/m', '22/10/1970', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Domenico Pavlov', 'dpavlovl@cmu.edu', 'dpavlovl', 'eN8{$,+(q', '24/04/1996', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Phyllys Petigrew', 'ppetigrewm@g.co', 'ppetigrewm', 'kI9>\qh}g6', '26/07/1985', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Irene Henaughan', 'ihenaughann@usda.gov', 'ihenaughann', 'rU4<ZD(i+r42`gHR', '09/05/1999', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Kenneth Sweetnam', 'ksweetnamo@netvibes.com', 'ksweetnamo', 'xB6"oh(ElOL(', '28/01/1976', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Falkner Cellier', 'fcellierp@meetup.com', 'fcellierp', 'oE2<DNh,C\eJ,pMQ', '10/03/1973', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Massimiliano Smorfit', 'msmorfitq@mayoclinic.com', 'msmorfitq', 'rW1,yS#7%gpTA"', '07/02/1998', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Rahel Dunabie', 'rdunabier@php.net', 'rdunabier', 'cJ2%IK"/O(S}w7/', '25/11/1964', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Stephie Bagot', 'sbagots@who.int', 'sbagots', 'lP5*Ba}H', '11/09/1978', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Olivia Ochterlonie', 'oochterloniet@state.tx.us', 'oochterloniet', 'tQ2~0B3b', '13/07/1983', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Simonne Roloff', 'sroloffu@fda.gov', 'sroloffu', 'vK4|.DJu57U/)2', '14/06/1983', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Jerrilee Craker', 'jcrakerv@mtv.com', 'jcrakerv', 'bB8*zb!""L@D|''(', '09/06/1960', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Rene Willmot', 'rwillmotw@rakuten.co.jp', 'rwillmotw', 'dH9~(#!Qh@K7', '07/09/1975', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Bree Brear', 'bbrearx@canalblog.com', 'bbrearx', 'dJ9|6"3uSBzFQE', '16/12/1987', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Sianna Sharpe', 'ssharpey@arizona.edu', 'ssharpey', 'sI8!TnQ4%UW\"', '14/07/1974', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Ardine Sibthorpe', 'asibthorpez@youku.com', 'asibthorpez', 'uW3(!DKV', '02/02/1986', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Lorrie Elton', 'lelton10@behance.net', 'lelton10', 'nI5+P~''TFwa=}A/<', '07/07/1964', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Casar Iban', 'ciban11@feedburner.com', 'ciban11', 'jF8(h*\dLShml{', '15/02/1974', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Duncan Juckes', 'djuckes12@purevolume.com', 'djuckes12', 'jQ0!?#.,,0R\)q', '03/03/1981', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Elwood Potbury', 'epotbury13@sun.com', 'epotbury13', 'hB4?Y~TK8z', '05/02/2004', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Enriqueta Sherwin', 'esherwin14@storify.com', 'esherwin14', 'hA4!''ynvZA,}R*', '25/02/1999', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Ulises Satford', 'usatford15@surveymonkey.com', 'usatford15', 'fN3\,"Z#p.rb5Nl', '15/02/1960', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Ricki Fearon', 'rfearon16@pen.io', 'rfearon16', 'xR4*.eGUh', '20/02/1978', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Perkin Spillett', 'pspillett17@fda.gov', 'pspillett17', 'zO8@!S(4eT2II', '11/09/1966', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Oswald Spurden', 'ospurden18@ucsd.edu', 'ospurden18', 'bV4*Y~"Zc1Xc6F', '25/05/1972', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Zaneta Pochet', 'zpochet19@guardian.co.uk', 'zpochet19', 'xA7/Um5SP', '30/08/2003', 'Currently renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Nikki Satterfitt', 'nsatterfitt1a@4shared.com', 'nsatterfitt1a', 'xD7>|ExT''z$/70', '16/06/1991', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Bernarr Baldacco', 'bbaldacco1b@google.ca', 'bbaldacco1b', 'kY9.U2~UH*QW?@K7', '04/12/1994', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Darrick Fillingham', 'dfillingham1c@latimes.com', 'dfillingham1c', 'gM3_rDWJIgYm20%', '17/06/1999', 'Currently not renting');
insert into lyfter_car_rental.users (full_name, email, user_name, password, date_of_birth, status_account) values ('Orson Knock', 'oknock1d@va.gov', 'oknock1d', 'yX2~uo?.QqR9\nOU', '02/06/1982', 'Currently renting');