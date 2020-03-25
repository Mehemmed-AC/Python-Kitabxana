    public boolean isdifadeciyoxlayici(String yeni_melumat, String durum) throws IOException{
        boolean bayrag_esas = false;
        boolean ozel_bayrag = false;
        int array_indexi = 0;
        String gizli_melumat_oxumaqucun;
        File isdifadecilerusers = new File("IsdifadecilerUsers.iu");
            if(!isdifadecilerusers.exists()){
                PrintWriter Fayila_Yaz = null;
                try {
                    Fayila_Yaz = new PrintWriter(isdifadecilerusers, "UTF-8");
                    
                } catch (FileNotFoundException | UnsupportedEncodingException e) {
                    consol.ConsolDaxiledici("XETA Isdifadeciler Fayili Yaradildiqi Zaman : <<< XETA isdifadeciyoxlayici");                
                }
                    //Ozel Method Yazilmasi lazimdir     
                    Fayila_Yaz.write("Default");
            } else{
                //Dosya_yaz(name_ad, "IsdifadecilerUsers.iu");
        }
        gizli_melumat_oxumaqucun = (String) Dosya_oxu("IsdifadecilerUsers.iu");    
        Scanner oxuyucu = new Scanner(gizli_melumat_oxumaqucun);
        while(oxuyucu.hasNext()){
            String setir = oxuyucu.nextLine();
            array[array_indexi] = setir;
            ++array_indexi;
        }
        for(int index = 0; index <= array.length; index++){
            if(array[index] == null){
                qutu = index;
                break;
            }
        }
        --qutu;
        for(int index = 0; index <= qutu; index++){
            String aciq_melumat = new String(decrypt(array[index].getBytes()));
            if(aciq_melumat.equals(yeni_melumat)){
                if(durum.equals("no standart")){
                      ozel_bayrag = true;
                      break;
                } else{                 
                    bayrag = false;
                    break;
                }
            } else{
                bayrag = true;
            }
        }    
        if(bayrag == false){
            Yazdir("\nBu ad Systemde var "+yeni_melumat);
            consol.ConsolDaxiledici("Bu ad Systemde var "+yeni_melumat+" <<< XETA isdifadeciyoxlayici");
            bayrag_esas = false;
        } else {
            if(!durum.equals("no standart")){         
                bayrag_esas = true;
                String gizli_melumat_yazmaqucun = new String(encrypt(gizli_melumat_oxumaqucun.getBytes()));     
                String gzili_yeni_melumat = new String(encrypt(yeni_melumat.getBytes()));
                gizli_melumat_yazmaqucun += ("\n"+gzili_yeni_melumat);
                Dosya_yaz((gizli_melumat_yazmaqucun), "IsdifadecilerUsers.iu");
            } else {
                bayrag_esas = ozel_bayrag;
            }
        }      
        return bayrag_esas;
    }
