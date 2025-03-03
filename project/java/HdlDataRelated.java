package None;

import java.util.List;
import lombok.*;






/**
  The data class for related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataRelated  {

  private String format;
  private List<Pid4CatRelation> value;

}
