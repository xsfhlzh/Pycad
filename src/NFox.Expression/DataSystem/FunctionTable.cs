
using NFox.Expression.SymbolValues;

namespace NFox.Expression.DataSystem
{

    public class FunctionTable : SymbolTable<Function>
    {

        protected override string Prefix
        {
            get { return "FunctionTable/"; }
        }

        protected override string Postfix
        {
            get { return ".fd"; }
        }
    }

}
