

using System;

namespace NFox.Geometry
{
    public static class GeoUtils
    {

        public static double EqualsPoint = 1e-10;
        public static double EqualsVector = 1e-12;
        public static double EqualsValue = 1e-10;

        public static double Round(double d)
        {
            var d2 = Math.Round(d, 10);
            if (Equals(d2, d))
                return d2;
            return d;
        }

        public static double Format(double value)
        {
            if (Math.Abs(value) < EqualsValue)
                value = 0;
            return value;
        }

        public static bool Equals(double v1, double v2)
        {
            return Math.Abs(v1 - v2) < EqualsValue;
        }

        public static bool Equals(float v1, float v2)
        {
            return Math.Abs(v1 - v2) < EqualsValue;
        }

        public static bool Equals(double v1, double v2, double tol)
        {
            return Math.Abs(v1 - v2) < tol;
        }

        public static void Swap(ref double[,] mat, int x1, int y1, int x2, int y2)
        {
            double value = mat[x1, y1];
            mat[x1, y1] = mat[x2, y2];
            mat[x2, y2] = value;
        }

        /// <summary>
        /// 获取逆矩阵
        /// </summary>
        /// <returns></returns>
        public static bool Inverse(ref double[,] mat, int n)
        {

            int[] iis = new int[n];
            int[] jjs = new int[n];

            for (int k = 0; k < n; k++)
            {
                // 第一步，全选主元
                double fMax = 0.0;
                for (int i = k; i < n; i++)
                {
                    for (int j = k; j < n; j++)
                    {
                        double f = Math.Abs(mat[i, j]);
                        if (f > fMax)
                        {
                            fMax = f;
                            iis[k] = i;
                            jjs[k] = j;
                        }
                    }
                }
                if (Math.Abs(fMax) < GeoUtils.EqualsValue)
                    return false;

                if (iis[k] != k)
                {
                    for (int i = 0; i < n; i++)
                        Swap(ref mat, k, i, iis[k], i);
                }

                if (jjs[k] != k)
                {
                    for (int i = 0; i < n; i++)
                        Swap(ref mat, i, k, i, jjs[k]);
                }

                // 第二步
                mat[k, k] = 1.0 / mat[k, k];

                // 第三步
                for (int j = 0; j < n; j++)
                {
                    if (j != k)
                        mat[k, j] *= mat[k, k];
                }
                // 第四步
                for (int i = 0; i < n; i++)
                {
                    if (i != k)
                    {
                        for (int j = 0; j < n; j++)
                        {
                            if (j != k)
                                mat[i, j] = mat[i, j] - mat[i, k] * mat[k, j];
                        }
                    }
                }
                // 第五步
                for (int i = 0; i < n; i++)
                {
                    if (i != k)
                        mat[i, k] *= -mat[k, k];
                }
            }

            for (int k = n - 1; k >= 0; k--)
            {
                if (jjs[k] != k)
                {
                    for (int i = 0; i < n; i++)
                        Swap(ref mat, k, i, jjs[k], i);
                }
                if (iis[k] != k)
                {
                    for (int i = 0; i < n; i++)
                        Swap(ref mat, i, k, i, iis[k]);
                }
            }

            return true;

        }




    }

}
