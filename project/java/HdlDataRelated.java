package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  The data class for related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataRelated  {

  private String format;
  private List<Pid4CatRelation> value;

}
