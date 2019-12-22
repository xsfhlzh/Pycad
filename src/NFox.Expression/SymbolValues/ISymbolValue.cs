
using NFox.Expression.DataSystem;
namespace NFox.Expression.SymbolValues
{
    public interface ISymbolValue : IParser
    {
        string Name { get; }
        Database Database { set; get; }
        SymbolIndex Index { set; get; }
        //string Dict { set; get; }
    }
}
