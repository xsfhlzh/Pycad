
namespace NFox.Geometry
{

    public abstract class Curve2D : Entity2D
    {
        public abstract bool Closed { get; }
        public abstract double Length { get; }
        public abstract double StartParam { get; }
        public abstract double EndParam { get; }
        public abstract Point2D GetPointAtParam(double par);
    }

}
