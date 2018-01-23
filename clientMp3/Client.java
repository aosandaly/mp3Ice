import app.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Client
{
    public static void main(String[] args)
    {
        try(com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize(args))
        {
            com.zeroc.Ice.Properties datasize = com.zeroc.Ice.Util.createProperties();
            datasize.setProperty("Ice.MessageSizeMax", "100024");
            com.zeroc.Ice.InitializationData initData = new com.zeroc.Ice.InitializationData();
            initData.properties = datasize;
            com.zeroc.Ice.Communicator ic = com.zeroc.Ice.Util.initialize(initData);

            com.zeroc.Ice.ObjectPrx base = ic.stringToProxy("Server:tcp -h 127.0.0.1 -p 10000");
            ServerPrx server = ServerPrx.checkedCast(base);
            if(server == null)
            {
                throw new Error("Invalid proxy");
            }

            int inputChoose=-1;
            do{
                System.out.println("Mon lecteur mp3 :");
                System.out.println("1. Ajouter une musique");
                System.out.println("2. Rechercher une musique(avec critere)");
                System.out.println("3. Supprimer une musique");
                System.out.println("4. Afficher les musiques");
                System.out.println("5. Quitter l'application");
                System.out.println("6. Download une musique (en test)");
                System.out.println("");
                System.out.print("Choisir une option entre 1 et 5\r\n");

                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                Scanner kb = new Scanner(System.in);

                try {

                    do{
                        try {
                            inputChoose = Integer.parseInt(kb.nextLine());
                            break;
                        } catch (NumberFormatException nfe) {
                            System.out.print("Try again: ");
                            inputChoose=-1;
                        }
                    }while((inputChoose>0)&&(inputChoose<6));

//                    inputChoose = num1;
                    while((inputChoose < 0)|| (inputChoose > 6))
                    {
                        System.out.println("Option invalide retapez la saisi !");
                        inputChoose = Integer.parseInt(br.readLine());
                    }

                    switch (enumMenu.getIdToEnum(inputChoose)) {
                        case ADD:
                            System.out.print("\033[H\033[2J");

                            System.out.println("Entrer les métadata de la musique");
                            System.out.println("");

                            System.out.println("Le titre :");
                            String name = br.readLine();

                            System.out.println("Le genre :");
                            String genre = br.readLine();

                            System.out.println("L'auteur :");
                            String author = br.readLine();

                            System.out.println("L'url :");
                            String url = br.readLine();

                            music oneMusic = new music(name, genre, author, url);
                            System.out.println(server.addDocument(oneMusic));

                            break;
                        case SEARCH:
                            System.out.print("\033[H\033[2J");
                            System.out.println("Rechercher une musique");
                            System.out.println("1 - Titre");
                            System.out.println("2 - Genre");
                            System.out.println("3 - Auteur");
                            System.out.println("4 - Url");
                            System.out.println("Choisir le n° du critère : ");
                            int idCritere = Integer.parseInt(br.readLine());
                            String critere = enumFilter.getIdToCritere(idCritere);

                            System.out.println("Choisir la valeur du critère");
                            String critereValue = br.readLine();
                            app.music[] musics = server.searchDocument(critere, critereValue);

                            if (musics.length == 0) {
                                System.out.println("Aucune music ne correspond a votre recherche");
                            } else {
                                System.out.println("Titre || genre || auteur || url");

                                for (app.music music : musics) {
                                    System.out.println(music.name + "         " + music.genre + "      " + music.author + "           " + music.url);
                                }
                            }
                            break;
                        case DEL:
                            System.out.print("\033[H\033[2J");
                            System.out.println("Donner le nom de la musique à supprimer");
                            String input3 = br.readLine();
                            if (input3.equals("")) {
                                System.out.println("Saisir le nom de la musique pour supprimer");
                            } else {
                                musics = server.searchDocument("name", input3);
                                if (musics.length != 0) {
                                    System.out.println(server.removeDocument(input3));
                                    System.out.println("\n");
                                    System.out.println("La liste après la suppression d'une music donner en paramettre");
                                    System.out.println("Titre || genre || auteur || url");
                                    for (app.music music : server.displayListMusic()) {
                                        System.out.println(music.name + "         " + music.genre + "      " + music.author + "           " + music.url);
                                    }
                                } else {
                                    System.out.println("La liste est vide ou le nom saisie n'existe pas sur le serveur");
                                }
                            }
                            break;
                        case DISPLAY:
                            System.out.print("\033[H\033[2J");
                            if (server.displayListMusic().length == 0) {
                                System.out.println("La liste des musiques est vide");
                            } else {
                                System.out.println("------------ Les musiques du serveur en cours ------------");
                                System.out.println("");
                                System.out.println("Titre || genre || auteur || url");
                                for (app.music music : server.displayListMusic()) {
                                    System.out.println(music.name + "         " + music.genre + "      " + music.author + "           " + music.url);
                                }
                            }
                            break;
                        case QUIT:
                            System.exit(1);
                            break;
                        case DOWNLOAD:
                            System.out.print("\033[H\033[2J");
                            System.out.print("en test");
                           //app.music result = null;
                            //byte[] file = server.downloadDocument(result);
                            break;
                        default:
                            System.out.println("Option invalide !\r\n");
                    }
                } catch (IOException ioe) {
                    System.out.println("IO error trying to read your input!\r\n");
                    System.exit(1);
                }
                catch (NumberFormatException ie) {
                    System.out.println("fr!\r\n");
                }
            }while(inputChoose != 6);

        }
    }
}