
namespace NFox.Geometry
{
    public interface IEntityProvider
    {
        object ToObject(Entity2D entity);
        Entity2D FromObjet(object obj);
    }
}
