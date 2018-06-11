using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Office.Tools.Excel;

namespace toto
{
    public static class hesapla
    {


            static List<int> hatalar;
            static List<List<int[,]>> tumfiltreler;
            static int[] currkupon;
            static CheckBox[,] cati;
            static List<string> kuponlar;
        static bool ol;


            public static int kacadet(int[][] args,int maxhata, CheckBox[,] catia,bool olum)
            {

            kuponlar = new List<string>();

            ol = olum;

            cati = catia;
                hatalar = new List<int>();
                tumfiltreler = new List<List<int[,]>>();

                currkupon = new int[15];



                for (int i = 0; i <= maxhata; i++)
                {
                    hatalar.Add(i);
                }


                for (int i = 0; i < 14; i++)
                {
                    tumfiltreler.Add(new List<int[,]>());
                }


                int max = 14;

                for (int i = 0; i < 14; i++)
                {

                    for (int a = 0; a < max - i; a++)
                    {
                        int[,] f = new int[3, 3];

                    var bas1 = i * 3;
                    var bas2 =i*3+a*3;


                        f[0, 0] = args[bas1+1][bas2+1];
                        f[0, 1] = args[bas1+1][bas2];
                        f[0, 2] = args[bas1+1][bas2 + 2];
                        f[1, 0] = args[bas1][bas2+1];
                        f[1, 1] = args[bas1][bas2]; ;
                        f[1, 2] = args[bas1][bas2 + 2]; ;
                        f[2, 0] = args[bas1+2][bas2+1 ]; ;
                        f[2, 1] = args[bas1+2][bas2]; ;
                        f[2, 2] = args[bas1+2][bas2 + 2]; ;





                    tumfiltreler[i].Add(f);



                    }



                }

            int s0, s1, s2;
            s0 = 0;s1 = 0;s2 = 0;

            if (cati[0,1].Checked)
            {
                s0 = Kuponsayi(0, 0, 0);
            }
            if (cati[0, 0].Checked)
            {
                s1 = Kuponsayi(0, 1, 0);
            }

            if (cati[0, 2].Checked)
            {
                s2 = Kuponsayi(0, 2, 0);
            }

            string path = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);

            System.IO.Directory.CreateDirectory(path+"\\kuponlar");



            if (kuponlar.Count<100000 && ol)
            {


                System.IO.StreamWriter file = new System.IO.StreamWriter(path + "\\kuponlar\\" + "kupon.txt");
                foreach (var item in kuponlar)
                {
                    file.WriteLine(item);
                }

                file.Close();


            }












            return s0 + s1 + s2;



            }

            static int Kuponsayi(int level, int sonuc, int hatasayisi)
            {



                currkupon[level] = sonuc;

                for (int i = 0; i <= level - 1; i++)
                {
                    if (tumfiltreler[i][level - i - 1][currkupon[i], sonuc] == 1)
                    {
                        hatasayisi++;
                    }
                }

                if (!hatalar.Contains(hatasayisi))
                {
                    return 0;
                }


                if (level == 14)
                {
                //Console.WriteLine(string.Join("-", currkupon));

                    if (ol)
                    {
                        kuponlar.Add(string.Join("-",currkupon));
                    }
                    return 1;
                }

            int s0, s1, s2;
            s0 = 0;s1 = 0;s2 = 0;

            if (cati[level+1, 1].Checked)
            {
                s0 = Kuponsayi(level+1, 0, hatasayisi);
            }

            if (cati[level + 1, 0].Checked)
            {
                s1 = Kuponsayi(level+1, 1, hatasayisi);
            }

            if (cati[level + 1, 2].Checked)
            {
                s2 = Kuponsayi(level+1, 2, hatasayisi);
            }





            return s0 + s1 + s2;




            }


        }

    }

